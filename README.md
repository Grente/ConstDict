# ConstDict

python节省内存的字典数据结构
若字典不会增加字段，只读/原字段修改
使用ConstDict可节省内存


Dict()内存主要消耗的地方：
1、Dict扩容机制，预留内存空间
2、Dict也是一个对象，内部会动态维护__dict__，增加slot类属性可以节省内容



节省内存大小：一半以上,字段越大节省越多


适用场景：需要生成大量的静态字典场景
缺点：根据字典的属性，生成类对象，再生产对象


python版本：python2.7


例子：

```
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


>>> test_dic = {
...     "m_HP": 1,
...     "m_MP": 2,
...     "m_Attack": 3,
...     "m_Defense": 4,
...     "m_Speed": 5,
...     "m_Dodge": 6,
...     "m_Hit": 7,
...     "m_Double": 8,
... }
>>>
>>> class MonsterDict(constdict.ConstDict):
...     __slots__ = test_dic.keys()
    

>>> const_dic = MonsterDict(test_dic)
>>> print(asizesof(test_dic))
(1192,)
>>> print(asizesof(const_dic))
(584,)


>>> print(const_dic)
{'m_Defense': 4, 'm_Speed': 5, 'm_Hit': 7, 'm_Double': 8, 'm_Attack': 3, 'm_HP': 1, 'm_Dodge': 6, 'm_MP': 2}


>>> print(const_dic.keys())
['m_HP', 'm_Defense', 'm_Speed', 'm_Attack', 'm_Dodge', 'm_MP', 'm_Hit', 'm_Double']


>>> print(const_dic.values())
[1, 4, 5, 3, 6, 2, 7, 8]


>>> const_dic["m_Dodge"] = 12456
>>> print(const_dic["m_Dodge"])
12456


>>> print(const_dic.iteritems())
<generator object <genexpr> at 0x00000000094FA2C8>
```








