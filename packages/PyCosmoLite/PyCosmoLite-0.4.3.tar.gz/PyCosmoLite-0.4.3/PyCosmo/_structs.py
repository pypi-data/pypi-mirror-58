# Copyright (C) 2013 ETH Zurich, Institute for Astronomy

'''
Created on Mar 4, 2014

author: jakeret
'''

from __future__ import print_function, division, absolute_import, unicode_literals

import numpy as np
import six

if six.PY3:

    import collections

    class ImmutableStructSuper(collections.MutableMapping):
        pass

else:

    import UserDict

    class ImmutableStructSuper(object, UserDict.DictMixin):
        pass


# In Python 2.7 still, `DictMixin` is an old-style class; thus, we need
# to make `Struct` inherit from `object` otherwise we loose properties
# when setting/pickling/unpickling


class ImmutableStruct(ImmutableStructSuper):
    """
    A `dict`-like object, whose keys can be accessed with the usual
    '[...]' lookup syntax, or with the '.' get attribute syntax.

    Examples::

      >>> a = Struct()
      >>> a['x'] = 1
      >>> a.x
      1
      >>> a.y = 2
      >>> a['y']
      2

    Values can also be initially set by specifying them as keyword
    arguments to the constructor::

      >>> a = Struct(z=3)
      >>> a['z']
      3
      >>> a.z
      3

    Like `dict` instances, `Struct`s have a `copy` method to get a
    shallow copy of the instance:

      >>> b = a.copy()
      >>> b.z
      3

    """
    def __init__(self, initializer=None, **extra_args):
        if initializer is not None:
            try:
                # initializer is `dict`-like?
                for name, value in initializer.items():
                    self.__dict__[name] = value
            except AttributeError:
                # initializer is a sequence of (name,value) pairs?
                for name, value in initializer:
                    self.__dict__[name] = value
        for name, value in extra_args.items():
            self.__dict__[name] = value

    def copy(self):
        """Return a (shallow) copy of this `Struct` instance."""
        return ImmutableStruct(self)

    # the `DictMixin` class defines all std `dict` methods, provided
    # that `__getitem__`, `__setitem__` and `keys` are defined.
    def __setitem__(self, name, val):
        raise ValueError("Trying to modify immutable struct with: %s=%s"%(str(name), str(val)))

    def __getitem__(self, name):
        return self.__dict__[name]

    def keys(self):
        return self.__dict__.keys()

    def __str__(self):
        str = "{\n"
        for name, value in sorted(self.items()):
            str += ("  %s='%s'\n" %(name, value))
        str += "}"
        return str

    def __eq__(self, other):
        if set(self.__dict__.keys()) != set(other.__dict__.keys()):
            return False
        for name, value in self.__dict__.items():
            other_value = other.__dict__[name]
            if isinstance(value, float) and isinstance(other_value, float):
                if np.isnan(value) and np.isnan(other_value):
                    continue
            if value != other_value:
                return False
        return True

    def __iter__(self):
        return iter(self.__dict__)

    def __delitem__(self, *args, **kwargs):
        pass

    def __len__(self):
        pass


class Struct(ImmutableStruct):
    """
    Mutable implementation of a Strcut
    """


    def __setitem__(self, name, val):
        self.__dict__[name] = val

    def copy(self):
        """Return a (shallow) copy of this `Struct` instance."""
        return Struct(self)

