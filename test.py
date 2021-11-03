# -*- coding: utf-8 -*-

from pympler.asizeof import asizesof
import constdict


test_dic = {
    "m_HP": 1,
    "m_MP": 2,
    "m_Attack": 3,
    "m_Defense": 4,
    "m_Speed": 5,
    "m_Dodge": 6,
    "m_Hit": 7,
    "m_Double": 8,
}

class MonsterDict(constdict.ConstDict):
    __slots__ = test_dic.keys()
    

if __name__ == "__main__":
    const_dic = MonsterDict(test_dic)
    
print(asizesof(test_dic))
print(asizesof(const_dic))


print(const_dic)

print(const_dic.keys())
print(const_dic.values())

const_dic["m_Dodge"] = 12456
print(const_dic["m_Dodge"])
print(const_dic.iteritems())



