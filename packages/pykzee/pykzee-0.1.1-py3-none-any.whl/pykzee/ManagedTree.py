import asyncio
import collections
import functools
import inspect
import logging

from pyimmutable import ImmutableDict, ImmutableList

from pykzee.common import (
    PathType,
    Undefined,
    call_soon,
    makePath,
    pathToString,
    setDataForPath,
    getDataForPath,
)
from pykzee import AttachedInfo
from pykzee.Plugin import Plugin
from pykzee.Tree import Tree


SubscriptionSlot = collections.namedtuple(
    "SubscriptionSlot", ("path", "directory", "resolve_symlinks")
)


class Subscription:
    __slots__ = (
        "plugin",
        "slots",
        "callback",
        "__currentState",
        "__reportedState",
        "disabled",
    )

    def __init__(self, plugin, slots, callback, state, initial: bool):
        if (
            type(slots) != tuple
            or any(type(slot) is not SubscriptionSlot for slot in slots)
            or type(state) != ImmutableList
            or not len(slots) == len(state)
        ):
            logging.error(  # FIXME REMOVE
                "Subscription constructor called with invalid arguments: "
                f"slots={ slots !r} len(state)={ len(state) }"
            )
            raise Exception(
                "Subscription constructor called with invalid arguments: "
                f"slots={ slots !r} len(state)={ len(state) }"
            )
        self.plugin = plugin
        self.slots = slots
        self.callback = callback
        self.__currentState = state
        self.__reportedState = (
            ImmutableList(Undefined for _ in slots) if initial else state
        )
        self.disabled = False

    def setCurrentState(self, idx, state):
        self.__currentState = self.__currentState.set(idx, state)

    def needsUpdate(self):
        return self.__reportedState is not self.__currentState

    def updated(self):
        self.__reportedState = self.__currentState

    def getState(self):
        return self.__currentState


class Mount:
    __slots__ = "plugin", "directory", "tree", "disabled"

    def __init__(self, plugin, directory, tree):
        self.plugin = plugin
        self.directory = directory
        self.tree = tree
        self.disabled = False


class Directory:
    __slots__ = "parent pathElement subdirectories".split()

    def __init__(self, parent, path_element):
        self.parent = parent
        self.pathElement = path_element
        self.subdirectories = {}

    def get(self, path: PathType, *, create=True):
        d = self
        for p in path:
            sd = d.subdirectories.get(p)
            if sd is None:
                if create:
                    sd = d.subdirectories[p] = type(self)(d, p)
                else:
                    return
            d = sd
        return d

    def garbageCollect(self):
        parent = self.parent
        if (
            parent is not None
            and not self.subdirectories
            and self._canBeRemoved()
        ):
            del parent.subdirectories[self.pathElement]
            self.parent = None
            parent.garbageCollect()


class SubscriptionDirectory(Directory):
    __slots__ = ("subscriptions", "state")

    def __init__(self, parent, path_element):
        super().__init__(parent, path_element)
        self.subscriptions = set()  # (sub, idx) tuples
        self.state = Undefined
        try:
            if type(parent.state) in (ImmutableDict, ImmutableList):
                self.state = parent.state[path_element]
        except Exception:
            ...

    def _canBeRemoved(self):
        return not self.subscriptions

    def update(self, new_state):
        if new_state is self.state:
            return

        for sub, idx in self.subscriptions:
            sub.setCurrentState(idx, new_state)

        for key, subdir in self.subdirectories.items():
            sdata = Undefined
            if type(new_state) in (ImmutableDict, ImmutableList):
                try:
                    sdata = new_state[key]
                except Exception:
                    ...

            subdir.update(sdata)

        self.state = new_state


class MountDirectory(Directory):
    __slots__ = ("mount",)

    def __init__(self, parent, path_element):
        super().__init__(parent, path_element)
        self.mount = None

    def _canBeRemoved(self):
        return self.mount is None


class Command:
    __slots__ = "path", "name", "function", "doc", "disabled"

    def __init__(self, path, name, function, doc):
        self.path = path
        self.name = name
        self.function = function
        self.doc = doc
        self.disabled = False


class PluginInfo:
    __slots__ = "subscriptions", "mounts", "plugInsAdded", "disabled", "plugin"

    def __init__(self):
        self.subscriptions = set()
        self.mounts = set()
        self.plugInsAdded = set()
        self.disabled = False


class ManagedTree:
    __slots__ = """
    __state __resolvedState __root __resolvedRoot __realpath
    __mountRoot __pluginInfos __commands
    __subscriptionCheckScheduled __subscriptionCheckLock
    __coreSet
    """.strip().split()

    def __init__(self):
        self.__state = self.__resolvedState = ImmutableDict()
        self.__root = SubscriptionDirectory(None, None)
        self.__resolvedRoot = SubscriptionDirectory(None, None)
        self.__realpath = makePath
        self.__mountRoot = MountDirectory(None, None)
        self.__pluginInfos = set()
        self.__commands = {}  # path -> {name: Command}
        self.__subscriptionCheckScheduled = False
        self.__subscriptionCheckLock = asyncio.Lock()

        # We will be writing internal information to "/core", so make sure
        # no plug-in can interfere
        self.__mountRoot.get(("core",)).mount = True
        self.__coreSet = lambda path, value: self.set(("core",) + path, value)

    def get(self, path: PathType, *, resolve_symlinks=True):
        return getDataForPath(
            self.__resolvedState if resolve_symlinks else self.__state, path
        )

    def set(self, path: PathType, value):
        new_state = setDataForPath(self.__state, path, value)
        if not new_state.isImmutableJson:
            raise Exception("invalid data")
        if self.__state is new_state:
            return
        new_state = setDataForPath(
            new_state,
            ("core", "symlinks"),
            AttachedInfo.symlinkInfoDict(new_state),
        )
        self.__resolvedState = AttachedInfo.resolved(new_state)
        self.__realpath = (lambda func: lambda path: func(makePath(path)))(
            AttachedInfo.realpath(new_state)
        )
        self.__state = new_state

        self.__scheduleSubscriptionCheck()
        print(sorted(new_state.meta))

    def command(self, path, cmd):
        return self.__commands[path][cmd].function

    def subscribe(
        self,
        plugin_info,
        paths,
        callback,
        *,
        initial=True,
        resolve_symlinks=True,
    ):
        if plugin_info.disabled or plugin_info not in self.__pluginInfos:
            raise Exception("disabled/unregistered plugin must not subscribe")
        slots = tuple(
            SubscriptionSlot(
                path,
                (self.__resolvedRoot if resolve_symlinks else self.__root).get(
                    path
                ),
                resolve_symlinks,
            )
            for path in paths
        )
        state = ImmutableList(slot.directory.state for slot in slots)
        sub = Subscription(plugin_info, slots, callback, state, initial)
        plugin_info.subscriptions.add(sub)
        for idx, slot in enumerate(slots):
            slot.directory.subscriptions.add((sub, idx))
        if initial:
            self.__scheduleSubscriptionCheck()
        return lambda: self.unsubscribe(sub)

    def unsubscribe(self, sub):
        sub.disabled = True
        for idx, slot in enumerate(sub.slots):
            slot.directory.subscriptions.discard((sub, idx))
            slot.directory.garbageCollect()
        sub.plugin.subscriptions.discard(sub)

    def mount(self, plugin_info, path):
        directory = self.__mountRoot.get(path)
        if any(d.mount for d in self.__relatedDirectories(directory)):
            directory.garbageCollect()
            raise Exception("conflicting mount")

        mount = Mount(plugin_info, directory, Tree(self, path))
        plugin_info.mounts.add(mount)
        directory.mount = mount
        return mount.tree.getAccessProxy()._replace(
            deactivate=functools.partial(self.unmount, mount)
        )

    def unmount(self, mount):
        if mount.disabled:
            return
        mount.disabled = True
        mount.directory.mount = None
        mount.plugin.mounts.discard(mount)
        mount.tree.deactivate()
        mount.directory.garbageCollect()

    def registerCommand(self, path, name, function, doc=Undefined):
        if doc is Undefined:
            doc = function.__doc__
        sig = inspect.signature(function)
        cmd = Command(path, name, function, doc)
        try:
            path_commands = self.__commands[path]
        except KeyError:
            path_commands = self.__commands[path] = {}
        if name in path_commands:
            raise Exception("Command { path }:{ name } already registered")
        path_commands[name] = cmd

        self.__coreSet(
            ("commands", pathToString(path), name),
            {"doc": doc, "signature": str(sig)},
        )

        def unregisterCommand():
            if cmd.disabled:
                return
            cmd.disabled = True
            path_commands = self.__commands[cmd.path]
            path_commands.pop(cmd.name)
            if not path_commands:
                del self.__commands[cmd.path]
                self.__coreSet(("commands", pathToString(cmd.path)), Undefined)
            else:
                self.__coreSet(
                    ("commands", pathToString(cmd.path), cmd.name), Undefined
                )

        return unregisterCommand

    def addPlugin(
        self, PluginType: type, added_by: PluginInfo, *args, **kwargs
    ):
        if added_by is not None:
            if added_by.disabled:
                raise Exception("Disabled plugin tried to register a plugin")
            if added_by not in self.__pluginInfos:
                raise Exception("Parent plugin not registered with this tree")
        if not issubclass(PluginType, Plugin):
            raise TypeError("Plugin type must derive from Plugin class")
        plugin_info = PluginInfo()
        plugin_info.plugin = PluginType(
            get=lambda path: self.get(path),
            subscribe=lambda callback, *paths, initial=True: self.subscribe(
                plugin_info, paths, callback, initial=initial
            ),
            mount=lambda path: self.mount(plugin_info, path),
            addPlugin=lambda PluginType, *args, **kwargs: self.addPlugin(
                PluginType, plugin_info, *args, **kwargs
            ),
            removePlugin=lambda: self.__removePlugin(plugin_info),
            command=lambda path, cmd: self.command(path, cmd),
        )
        self.__pluginInfos.add(plugin_info)
        if added_by is not None:
            added_by.plugInsAdded.add(plugin_info)
        init = getattr(plugin_info.plugin, "init", None)
        if init is not None:
            call_soon(init, *args, **kwargs)
        elif args or kwargs:
            logging.warning("plugin has no init method - ignoring arguments")
        return lambda: self.__removePlugin(plugin_info)

    def __removePlugin(self, plugin_info):
        if plugin_info.disabled:
            return
        self.__pluginInfos.remove(plugin_info)
        plugin_info.disabled = True

        for p in plugin_info.plugInsAdded:
            self.__removePlugin(p)

        plugin_info.subscriptions = set()
        for sub in plugin_info.subscriptions:
            self.unsubscribe(sub)

        plugin_info.mounts = set()
        for mount in plugin_info.mounts:
            self.unmount(mount)

        shutdown = getattr(plugin_info.plugin, "shutdown", None)
        if shutdown is not None:
            call_soon(shutdown)

    def __scheduleSubscriptionCheck(self):
        if not self.__subscriptionCheckScheduled:
            self.__subscriptionCheckScheduled = True
            call_soon(self.__subscriptionCheck)

    async def __subscriptionCheck(self):
        async with self.__subscriptionCheckLock:
            self.__subscriptionCheckScheduled = False

            self.__root.update(self.__state)
            self.__resolvedRoot.update(self.__resolvedState)

            for sub in list(
                sub
                for plugin_info in self.__pluginInfos
                for sub in plugin_info.subscriptions
            ):
                if sub.disabled:
                    continue
                if sub.needsUpdate():
                    call_soon(sub.callback, *sub.getState())
                    sub.updated()

    def __relatedDirectories(self, directory):
        yield directory

        parent = directory.parent
        while parent is not None:
            yield parent
            parent = parent.parent

        subdirs = list(directory.subdirectories.values())
        while subdirs:
            sd = subdirs.pop()
            yield sd
            subdirs.extend(sd.subdirectories.values())
