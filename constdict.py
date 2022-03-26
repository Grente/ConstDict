# -*- coding: utf-8 -*-


class ConstDict(object):
    __slots__ = []

    def __init__(self, dic):
        for key, val in dic.iteritems():
            setattr(self, key, val)

    def __iter__(self):
        return iter(self.__slots__)

    def __getitem__(self, item):
        if not isinstance(item, str):
            return None
        return getattr(self, item)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __contains__(self, item):
        return hasattr(self, item)
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return str(dict(self.items()))

    def get(self, key, default=None):
        return getattr(self, key, default)
    
    def update(self, dic):
        for key, val in dic.iteritems():
            if key in self.__slots__:
                setattr(self, key, val)
    
    def clear(self):
        for key in self.__slots__:
            if hasattr(self, key):
                delattr(self, key)
    
    def setdefault(self, key, val):
        if hasattr(self, key):
            return getattr(self, key)
        else:
            setattr(self, key, val)
            return val
    
    def pop(self, key, default=None):
        if hasattr(self, key):
            val = getattr(self, key)
            delattr(self, key)
            return val
        return default
        
    def iteritems(self):
        return iter(self.items())

    def items(self):
        return [(key, getattr(self, key, None)) for key in self.__slots__ if hasattr(self, key)]

    def iterkeys(self):
        return iter(self.keys())

    def itervalues(self):
        return iter(self.values())

    def keys(self):
        return [key for key in self.__slots__ if hasattr(self, key)]

    def values(self):
        return [getattr(self, key, None) for key in self.__slots__ if hasattr(self, key)]
