# -*- coding: utf-8 -*-
from __future__ import print_function

__all__ = ['KaryNode']


class NodeTypeErr(TypeError):
    def __init__(self, actual_object, expected_type):
        _msg = 'The type for argument "{}" was incorrect---of type "{}" should be instance of "{}".'
        actual_name = actual_object.__name__
        actual_type = type(actual_object)
        self.msg = _msg.format(actual_name, expected_type, actual_type)


class IterErr(AttributeError):
    def __init__(self, given_object):
        _msg = 'The object "{}" was assumed to be iterable.'
        given_name = given_object.__name__
        self.msg = _msg.format(given_name)


class AncestorNotFound(ValueError):
    def __init__(self, name):
        self.msg = 'Ancestor "{}" not found'.format(name)


class DescendantNotFound(ValueError):
    def __init__(self, name):
        self.msg = 'Descendent "{}" not found'.format(name)


def check_type(given_object, expected_type, expected_subtype=None):
    if not isinstance(given_object, expected_type):
        raise NodeTypeErr(given_object, expected_type)
    if expected_subtype and not hasattr(given_object, '__iter__'):
        raise IterErr(given_object)
    if expected_subtype is None:  # return if not going to check subtype
        return given_object
    if not isinstance(expected_subtype, type):
        raise NodeTypeErr(expected_subtype, type)
    for sub_object in given_object:
        check_type(sub_object, expected_subtype)
    return given_object


class KaryNode(object):
    def __init__(self, name, depends=None, ancestors=None):
        self._root = ancestors is None
        self.name = check_type(name, str)
        check_type(depends, list, str)
        self.depends = {}
        self._ancestors = []
        # check for non-default kwargs (None in place of mutable defaults for predictable behavior)
        if depends is not None:
            self.add(depends)
        if ancestors is not None:
            self._ancestors = ancestors

    def __repr__(self):
        return self.name

    def __iter__(self, include_self=True, reverse=False):
        # only include self in iteration for search when root to avoid double counting
        if self.is_root() and include_self:
            result = [self] + self.depends.values()
        else:
            result = self.depends.values()
        if reverse:
            result = reversed(result)
        return iter(result)

    def __str__(self):
        if self.is_leaf():
            return self.name
        else:
            frame_join = u'└─{}'
            subframe_pad = u'  {}'
            new_frame = []
            for node in self.__iter__(include_self=False, reverse=True):
                node_frame_rows = []
                frame_rows = str(node).split('\n')
                first_row = frame_rows.pop(0)
                node_frame_rows.append(frame_join.format(first_row))
                for frame_row in frame_rows:
                    node_frame_rows.append(subframe_pad.format(frame_row))
                new_frame.insert(0, '\n'.join(node_frame_rows))
                frame_join = u'├─{}'
                subframe_pad = u'│ {}'
            new_frame.insert(0, self.name)
            return '\n'.join(new_frame)

    def insert(self, ancestor_name, node_name):
        ancestor = self.search(ancestor_name)
        if ancestor is None:
            raise AncestorNotFound(ancestor_name)
        ancestor.add(node_name)

    def add(self, node_names):
        if not isinstance(node_names, list):
            node_names = [node_names]
        for name in node_names:
            self.depends[name] = KaryNode(name, ancestors=[])

    def add_ancestor(self, name):
        if self._ancestors is None:
            self._ancestors = [name]
        else:
            self._ancestors.append(name)

    def clear_ancestors(self):
        self._ancestors = []

    def lca(self, *node_names):
        nodes = [self.search(name) for name in node_names]
        nodes = [node for node in nodes if node is not None]
        if len(nodes) == 0:
            raise DescendantNotFound(node_names)
        min_ancestors = min([len(node._ancestors) for node in nodes])
        base_comparator = nodes.pop(0)
        last_matched_offset = 0
        for o in range(0 + 1, min_ancestors + 1):  # shift for negatives
            if all([base_comparator._ancestors[-o:] == node._ancestors[-o:] for node in nodes]):
                last_matched_offset = -o
                continue
            else:
                break
        if last_matched_offset != 0:
            return base_comparator._ancestors[last_matched_offset]

    def is_leaf(self):
        return len(self.depends) == 0

    def is_root(self):
        return self._root

    def search(self, name, include_self=True):
        for child in self.__iter__(include_self):
            if child.name == name:
                return child
            elif child.is_leaf():
                child.clear_ancestors()
                continue
            child = child.search(name, include_self=False)
            if isinstance(child, KaryNode):
                child.add_ancestor(self.name)
                return child
            else:
                continue
        # no such child found
        return
