# -*- coding: utf-8 -*-

class ConstDict(object):
    def __init__(self, dic):
        for key, val in dic.iteritems():
            setattr(self, key, val)

    def __iter__(self):
        return iter(self.__slots__)

    def __getitem__(self, item):
        return getattr(self, item, None)

    def __setitem__(self, key, value):
        return setattr(self, key, value)
    
    def __contains__(self, item):
        try:
            return getattr(self, item, False)
        except:
            return False
        
    def get(self, key, default):
        return getattr(self, key, default)

    def iteritems(self):
        return ((key, getattr(self, key, None)) for key in self.__slots__)

    def items(self):
        return [(key, getattr(self, key, None)) for key in self.__slots__]

    def iterkeys(self):
        return iter(self.__slots__)

    def itervalues(self):
        return (getattr(self, key, None) for key in self.__slots__)

    def keys(self):
        return self.__slots__

    def values(self):
        return [getattr(self, key, None) for key in self.__slots__]
    
    def update(self, dic):
        """
        const dict noly support exist keys update
        """
        for key, val in dic.iteritems():
            if getattr(self, key, False):
                setattr(self, key, val)
        raise NotImplementedError("ConstDictBase not support update")
    
    def __str__(self):
        return str(dict(self.items()))

