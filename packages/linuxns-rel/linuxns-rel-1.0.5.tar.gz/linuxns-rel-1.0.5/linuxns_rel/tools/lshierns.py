"""Discovers the available user or PID namespaces and prints them in
a tree hierarchy to the console."""

# Copyright 2018 Harald Albrecht
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied. See the License for the specific language governing
# permissions and limitations under the License.


import os
import pwd
from typing import Dict, List, Optional, Tuple, Union

import psutil

import asciitree
import asciitree.traversal
from asciitree.drawing import BoxStyle, BOX_LIGHT
from asciitree.traversal import Traversal

from linuxns_rel import (
    get_parentns, get_userns, get_owner_uid,
    CLONE_NEWUSER, CLONE_NEWPID)


class HierarchicalNamespaceIndex:
    """Index for hierarchical Linux kernel namespaces, specifically the
    PID and user hierarchical namespaces at this time."""

    def __init__(self, namespace_type: int, details: bool = False) -> None:
        """Sets up a hierarchical namespace index by discovering the
        available namespaces of the specific namespace type.

        :param namespace_type: type of hierarchical namespace, either
          `linuxns_rel.CLONE_NEWUSER` or `linuxns_rel.CLONE_NEWPID`.
        """
        if namespace_type == CLONE_NEWUSER:
            self._nstypename = 'user'
        elif namespace_type == CLONE_NEWPID:
            self._nstypename = 'pid'
        else:
            raise ValueError('unsupported namespace type')
        self._details = details
        # Dictionary of user/PID namespaces, indexed by their inode
        # numbers.
        self._index = dict() # type: Dict[int, 'HierarchicalNamespace']
        # Dictionary of root namespace(s), indexed by their inode
        # numbers (again). Normally, this should only show a single
        # root, unless we have limited visibility.
        self._roots = dict() # type: Dict[int, 'HierarchicalNamespace']
        self._discover_from_proc()
        self._discover_missing_parents()
        if self._details:
            self._discover_ownedns()

    def __getitem__(self, item: int) -> 'HierarchicalNamespace':
        """Looks up an hierarchical namespace object by its inode number
        identifier."""
        return self._index[item]

    @property
    def items(self) -> Dict[int, 'HierarchicalNamespace']:
        """The dict mapping namespace ids to HierarchicalNamespace objects."""
        return self._index

    def _get_owner(self, ns_f) -> Tuple[int, int]:
        """Given a hierarchical namespace reference, returns a tuple of
        the owner's user ID and user namespace inode number."""
        # Owner namespaces can be asked directly for their owner's
        # user ID
        if self._nstypename == 'user':
            try:
                owner_uid = get_owner_uid(ns_f)
            except OSError:
                owner_uid = -1
            return owner_uid, os.stat(ns_f.fileno()).st_ino
        # Sigh. This is getting more involved: get the owner namespace,
        # only then get the owner's user ID. Or not, thanks to our
        # "AWFULLY GREAT" namespace API. So "AWESOME".
        with get_userns(ns_f) as owner_f:
            try:
                owner_uid = get_owner_uid(owner_f)
            except OSError:
                owner_uid = -1
            return owner_uid, os.stat(owner_f.fileno()).st_ino

    def _discover_from_proc(self) -> None:
        """Discovers namespaces via `/proc/[PID]/ns/[TYPE]`."""
        # Never assume that this will locate *all* namespaces in the
        # hierarchy yet, but only those currently in use by
        # processes. In fact, since we're skimming the proc
        # filesystem, we may miss *user* namespaces, but I currently
        # lack to see a situation with hidden PID namespaces. Anyway,
        # in this first phase, we only collect namespaces, but don't
        # bother with the parent-child relationships.
        for process in psutil.process_iter():
            try:
                ns_ref = '/proc/%d/ns/%s' % (process.pid, self._nstypename)
                with open(ns_ref) as ns_f:
                    ns_id = os.stat(ns_f.fileno()).st_ino
                    if ns_id not in self._index:
                        owner_uid, ownerns_id = self._get_owner(ns_f)
                        proc_name = self._discover_proc_name(
                            process, ns_id)
                        self._index[ns_id] = HierarchicalNamespace(
                            ns_id, owner_uid, ownerns_id,
                            proc_name=proc_name,
                            nsref=ns_ref)
            except PermissionError:
                pass

    def _discover_ownedns(self) -> None:
        """Discovers non-user namespaces with their owning user namespaces."""
        namespaces = dict()  # type: Dict[int, Optional[]]
        for process in psutil.process_iter():
            try:
                for ns_type in ('cgroup', 'ipc', 'mnt', 'net', 'pid', 'uts'):
                    ns_ref = '/proc/%d/ns/%s' % (process.pid, ns_type)
                    ns_id = os.stat(ns_ref).st_ino
                    if ns_id not in namespaces:
                        namespaces[ns_id] = None
                        with get_userns(ns_ref) as owner_f:
                            owner_userns_id = os.stat(owner_f.fileno()).st_ino
                        proc_name = self._discover_proc_name(process, ns_id)
                        owner = self._index[owner_userns_id]
                        owner.owned_ns[ns_type].append(
                            Namespace(ns_id, ns_type, proc_name))
            except PermissionError:
                pass

    def _discover_proc_name(self, process: psutil.Process, ns_id: int) \
            -> Optional[str]:
        """Discovers the process "name" for a given process. The name is
        taken from the most senior process in the process tree which is
        still in the same (PID or user) namespace as the process
        initially specified to this function.
        """
        parent = process.parent()
        while parent:
            try:
                parent_ns_id = os.stat(
                    '/proc/%d/ns/%s' % (parent.pid, self._nstypename))\
                    .st_ino
            except PermissionError:
                parent_ns_id = -1
            if parent_ns_id != ns_id:
                break
            process = parent
            parent = process.parent()
        # prepare pretty-print process name: only use the last
        # executable path element, and strip of a leading "-" indicating
        # a login shell.
        try:
            proc_name = process.cmdline()[0].split('/')[-1]
        except IndexError:
            proc_name = "[%s]" % process.name()
        if proc_name[:1] == '-':
            proc_name = proc_name[1:]
        return '%s (%d)' % (proc_name, process.pid)

    def _discover_missing_parents(self) -> None:
        """."""
        # Next in phase two, we now discover the parent-child
        # relationships of the hierarchical namespaces discovered
        # during phase one. The unexpected surprise here is that we
        # may find parent namespaces that we didn't discover so far:
        # because these intermediate namespaces don't have any
        # process joined to them. But as these are hierarchical
        # namespaces you can't simply leave out an intermediate
        # namespace node. So we need to update the namespace index
        # while we iterate over a copy of it from phase one. This is
        # fine, as we recursively discover parent namespaces starting
        # from each namespace from phase one.
        for _, ns in self._index.copy().items():
            ns_ref = None
            try:
                ns_ref = open(ns.nsref)
                while ns_ref:
                    ns_id = os.stat(ns_ref.fileno()).st_ino
                    try:
                        parent_ns_ref = get_parentns(ns_ref)
                        parent_ns_id = os.stat(
                            parent_ns_ref.fileno()).st_ino
                        # Hoi! We might find out about parents we
                        # didn't know of so far from the process
                        # discovery phase. So we might need to add
                        # these newly found parents to our user
                        # namespace index.
                        if parent_ns_id not in self._index:
                            parent_uid, ownerns_id = self._get_owner(
                                parent_ns_ref)
                            self._index[parent_ns_id] = \
                                HierarchicalNamespace(parent_ns_id,
                                                      parent_uid,
                                                      ownerns_id)
                        # Wire up our parent-child namespace
                        # relationship.
                        self._index[ns_id].parent = \
                            self._index[parent_ns_id]
                    except PermissionError:
                        # No more parent, or the parent is out of our
                        # scope.
                        parent_ns_ref = None
                        if ns_id not in self._roots:
                            self._roots[ns_id] = self._index[ns_id]
                    # Release the current user namespace file
                    # reference, and switch over to the parent's user
                    #  namespace file reference.
                    ns_ref.close()
                    ns_ref = parent_ns_ref
            finally:
                # Whatever has happened, make sure to *not* leak (or,
                # rather waste) the user namespace file reference.
                if ns_ref:
                    ns_ref.close()

    class HierarchicalNamespaceTraversal(Traversal):
        """Traverses a tree of user namespace objects."""

        def __init__(self, namespace_type_name: str) -> None:
            super().__init__()
            self._namespace_type_name = namespace_type_name

        def get_root(self, tree: [Dict[int, 'HierarchicalNamespace']]) \
                -> 'HierarchicalNamespace':
            """Return the root node of a tree. In case we get more
            than a single root of user namespaces, we return a "fake"
            ro(o)t instead, which then contains the list/tuple of
            user namespaces. """
            if len(tree) == 1:
                return next(iter(tree.values()))
            fake_root = HierarchicalNamespace(0, 0, 0)
            fake_root.children = tree.values()
            return fake_root

        def get_children(self, node: Union['HierarchicalNamespace', 'Namespace']) \
                -> List['HierarchicalNamespace']:
            """Returns the list of child user namespaces for a user
            namespace node, or an empty list in case this is a str node."""
            if isinstance(node, Namespace):
                return []
            # A hierarchical namespace object might not only have child
            # namespaces, but also owned namespaces are shown as children.
            owned = [ns \
                for ns_type in ('cgroup', 'ipc', 'mnt', 'net', 'pid', 'uts') \
                    for ns in node.owned_ns[ns_type]]
            return sorted(owned, key=lambda n: "%s%d" % (n.ns_type, n.id)) + \
                sorted(node.children, key=lambda n: n.id)

        def get_text(self, node: Union['HierarchicalNamespace', 'Namespace']) -> str:
            """Returns the text for a user namespace node. It
            consists of the user namespace identifier (inode number).
            """
            if isinstance(node, Namespace):
                return "⟜ %s:[%d] process \"%s\"" % \
                    (node.ns_type, node.id, node.proc_name)
            # It's a hierarchical namespace object...
            if not node.id:
                return '?'
            if self._namespace_type_name == 'user':
                return '%s:[%d] process%s namespace-owning user "%s" (%d)' % (
                    self._namespace_type_name, node.id,
                    ' "%s"' % node.proc_name
                    if node.proc_name else '',
                    pwd.getpwuid(node.uid).pw_name, node.uid)
            return '%s:[%d] process%s owner user:[%d] "%s" (%d)' % (
                self._namespace_type_name, node.id,
                ' "%s"' % node.proc_name
                if node.proc_name else '',
                node.ownerns_id,
                pwd.getpwuid(node.uid).pw_name, node.uid)

    def render(self) -> None:
        """Renders an ASCII tree using our hierarchical namespace
        traversal object."""
        print(
            asciitree.LeftAligned(
                traverse=HierarchicalNamespaceIndex.
                HierarchicalNamespaceTraversal(self._nstypename),
                draw=BoxStyle(gfx=BOX_LIGHT, horiz_len=2)
            )(self._roots))


class Namespace: # pylint: disable=too-few-public-methods
    """A "flat" Linux namespace, identified by its inode number."""

    def __init__(self, nsid: int, nstype: str, proc_name: Optional[str] = None) -> None:
        """Represents a flat Linux namespace.

        :param nsid: the unique identifier of this namespace in form of an
          inode number.
        :param nstype: type of namespace, such as "net".
        :param proc_name: optional process name related to this namespace.
        """
        self.id = nsid
        self.ns_type = nstype
        self.proc_name = proc_name

class HierarchicalNamespace: # pylint: disable=too-many-instance-attributes,too-few-public-methods
    """A Linux user namespace, identified by its inode number, with
    the optional filesystem path where the user namespace can be
    referenced, at the hierarchical parent-child relations to other
    user namespaces."""

    def __init__(self, nsid: int, uid: int, ownerns_id: int, # pylint: disable=too-many-arguments
                 proc_name: Optional[str] = None,
                 nsref: Optional[str] = None) -> None:
        """Represents a Linux user namespace, together with its
        hierarchical parent-child relationships.

        :param nsid: the unique identifier of this user namespace in
          form of an inode number.
        :param uid: the user ID "owning" this user namespace.
        :param ownerns_id: the owning user namespace inode number.
        :param proc_name: optional process name related to this namespace.
        :param nsref: a filesystem path reference to this user or PID
          namespace, if known. Defaults to None, unless specified
          otherwise.
        """
        self.id = nsid
        self.nsref = nsref
        self.ownerns_id = ownerns_id
        self.owned_ns = dict()  # type: Dict[str, List[int]]
        for ns_type in ('cgroup', 'ipc', 'mnt', 'net', 'pid', 'uts'):
            self.owned_ns[ns_type] = []
        self.uid = uid
        self.proc_name = proc_name
        self._parent = None  # type: 'HierarchicalNamespace'
        self.children = []  # type: List['HierarchicalNamespace']

    @property
    def parent(self) -> 'HierarchicalNamespace':
        """Gets or sets the parent user namespace. Setting the parent
        will also add this user namespace to the children user
        namespaces of the parent user namespace.
        """
        return self._parent

    @parent.setter
    def parent(self, parent: 'HierarchicalNamespace') -> None:
        if not self._parent:
            self._parent = parent
            parent.children.append(self)


def lsuserns() -> None:
    """lsuserns CLI."""
    import argparse # pylint: disable=import-outside-toplevel

    parser = argparse.ArgumentParser(
        description='Show Linux user namespace tree.'
    )
    parser.add_argument(
        '-d', '--details', action='store_true',
        help='show details: owned non-user namespaces'
    )

    args = parser.parse_args()
    HierarchicalNamespaceIndex(CLONE_NEWUSER, args.details).render()


def lspidns() -> None:
    """lspidns CLI."""
    import argparse # pylint: disable=import-outside-toplevel

    parser = argparse.ArgumentParser(
        description='Show Linux PID namespace tree.'
    )

    args = parser.parse_args() # pylint: disable=unused-variable
    HierarchicalNamespaceIndex(CLONE_NEWPID).render()


# pylint: disable=protected-access
def graphns() -> None:
    """graphns CLI: discovers the PID and user namespace and then
    shows them as a graph in a new (SVG) viewer window.

    This requires PyQt5 to be installed, as well as graphviz.
    """
    from graphviz import Digraph # pylint: disable=import-outside-toplevel
    import linuxns_rel.tools.viewer as viewer # pylint: disable=import-outside-toplevel
    import argparse # pylint: disable=import-outside-toplevel

    parser = argparse.ArgumentParser(
        description='Show graphical Linux user+PID namespaces tree.'
    )
    parser.add_argument(
        '-d', '--details', action='store_true',
        help='show details: owned non-user namespaces'
    )

    args = parser.parse_args()
    pidns_index = HierarchicalNamespaceIndex(CLONE_NEWPID)
    userns_index = HierarchicalNamespaceIndex(CLONE_NEWUSER, args.details)

    def ns_node_id(xns: [HierarchicalNamespace, int], prefix: str) -> str:
        """Returns a unique, but predictable node identifier for a namespace."""
        if hasattr(xns, 'id'):
            return '%s-%d' % (prefix, xns.id)
        return '%s-%d' % (prefix, xns)

    def traverse_nodes(dot: Digraph, xns: HierarchicalNamespace,
                       prefix: str) -> None:
        """Traverse and render a tree of hierarchical namespaces, with
        owned non-user namespaces, if known."""
        dot.node(ns_node_id(xns, prefix),
                 '%s%s:[%d]' % (
                     '"%s"\n' % xns.proc_name if xns.proc_name else '',
                     prefix, xns.id),
                 style='filled',
                 fillcolor='#ffffff')
        for child in xns.children:
            traverse_nodes(dot, child, prefix)
        if xns.owned_ns:
            for ns_type in ('cgroup', 'ipc', 'mnt', 'net', 'uts'):
                if len(xns.owned_ns[ns_type]) > 1:
                    dot.node('owned-%s-%d' % (ns_type, xns.id), 
                             ns_type,
                             shape='folder',
                             style='filled')
                for ons in xns.owned_ns[ns_type]:
                    dot.node(ns_node_id(ons, ns_type),
                             '%s%s:[%d]' % (
                                 '"%s"\n' % ons.proc_name if ons.proc_name else '',
                                 ns_type, ons.id),
                             shape='box',
                             style='filled',
                             fillcolor='#ffffff')

    def traverse_relations(dot: Digraph, xns: HierarchicalNamespace,
                           prefix: str) -> None:
        if prefix != 'user':
            dot.edge(ns_node_id(xns, prefix),
                     ns_node_id(xns.ownerns_id, 'user'),
                     style='dashed',
                     constraint='false')
        for child in xns.children:
            dot.edge(ns_node_id(xns, prefix),
                     ns_node_id(child, prefix),
                     dir='back')
            traverse_relations(dot, child, prefix)
        if xns.owned_ns:
            for ns_type in ('cgroup', 'ipc', 'mnt', 'net', 'uts'):
                ownerid = ns_node_id(xns, prefix)
                if len(xns.owned_ns[ns_type]) > 1:
                    ownerid = 'owned-%s-%d' % (ns_type, xns.id)
                    dot.edge(ns_node_id(xns, prefix),
                             ownerid,
                             dir='back')
                for ons in xns.owned_ns[ns_type]:
                    dot.edge(ownerid,
                             ns_node_id(ons, ns_type),
                             dir='back')

    dot = Digraph('test',
                  comment='PID and USER namespaces',
                  format='png')
    dot.attr(rankdir='TB', newrank='true')

    with dot.subgraph(name='cluster_pid') as pid_cluster:
        with dot.subgraph(name='cluster_user') as user_cluster:
            # Configure the cluster subgraphs
            pid_cluster.attr(label='PID',
                             color='#85ad85',
                             style='filled',
                             fillcolor='#e6ffe6')
            user_cluster.attr(label='user',
                              color='#7598bd',
                              style='filled',
                              fillcolor='#e6f2ff')

            # Set all hierarchical namespace root elements to be on
            # the "same" rank, so GraphViz positions them at the same
            # level.
            with dot.subgraph(name='group') as g:
                g.attr(rank='same')
                for _, pid_ns in pidns_index._roots.items():
                    g.node(ns_node_id(pid_ns, 'pid'))
                for _, user_ns in userns_index._roots.items():
                    g.node(ns_node_id(user_ns, 'user'))

            # Now add all (remaining) nodes within each hierarchical
            # namespace.
            for _, pid_ns in pidns_index._roots.items():
                traverse_nodes(pid_cluster, pid_ns, 'pid')
            for _, user_ns in userns_index._roots.items():
                traverse_nodes(user_cluster, user_ns, 'user')

            # And finally add in the parent-child relationships, as
            # well as the owner relationships.
            for _, pid_ns in pidns_index._roots.items():
                traverse_relations(pid_cluster, pid_ns, 'pid')
            for _, user_ns in userns_index._roots.items():
                traverse_relations(user_cluster, user_ns, 'user')

    # Work around base64-encoded data URIs with mime type image/svg
    # not getting rendered when opened, but only after reloading.
    image = dot.pipe(format='svg')
    viewer.view(image)


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == '-g':
        graphns()
    else:
        lsuserns()
        lspidns()
