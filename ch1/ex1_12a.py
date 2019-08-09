#Counter是dict的子类，用于计数hashable对象

>>> from collections import Counter
>>> c=Counter()      #a new,empty counter
>>> c
Counter()
>>> c=Counter('gallahad')       #a new counter from an iterable
>>> c
Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})
>>> c=Counter({'red':4,'blue':2})    #a new counter from a mapping
>>> c
Counter({'red': 4, 'blue': 2})
>>> c=Counter({'red':4,'blue':2,'red':4})
>>> c
Counter({'red': 4, 'blue': 2})
>>> c = Counter(cats=4,dogs=8)     #a new counter from keyword args
>>> c
Counter({'dogs': 8, 'cats': 4})

#Counter对象有一个字典接口，如果引用的键没有任何记录，就返回一个0，而不是弹出一个 KeyError :
>>> c = Counter(['eggs','ham','ham'])
>>> c
Counter({'ham': 2, 'eggs': 1})
>>> c['bacon']
0
>>>


#设置一个计数为0不会从计数器中移去一个元素。使用 del 来删除它:
>>> c['sausage']=0
>>> c
Counter({'ham': 2, 'eggs': 1, 'sausage': 0})
>>> del c['sausage']
>>> c
Counter({'ham': 2, 'eggs': 1})
>>>


##返回一个迭代器,如果一个元素的计数小于1， elements() 就会忽略它。
>>> c = Counter(a=4,b=2,c=0,d=-2)
>>> c
Counter({'a': 4, 'b': 2, 'c': 0, 'd': -2})
>>> c.elements()
<itertools.chain object at 0x7f63344a8160>
>>> sorted(c.elements())
['a', 'a', 'a', 'a', 'b', 'b']

#返回一个列表，提供 n 个频率最高的元素和计数  most_common(n)   相等个数的元素顺序随机：
>>> Counter('abracadabra').most_common(3)
[('a', 5), ('b', 2), ('r', 2)]

#subtract([iterable-or-mapping])   从 迭代对象 或 映射对象 减去元素
>>> c = Counter(a=4, b=2, c=0, d=-2)
>>> d = Counter(a=1, b=2, c=3, d=4)
>>> c.subtract(d)
>>> c
Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

#加和减，结合计数器，通过加上或者减去元素的相应计数。交集和并集返回相应计数的最小或最大值。每种操作都可以接受带符号的计数，但是输出会忽略掉结果为零或者小于零的计数。
>>> c = Counter(a=3, b=1)
>>> d = Counter(a=1, b=2)
>>> c + d                       # add two counters together:  c[x] + d[x]
Counter({'a': 4, 'b': 3})
>>> c - d                       # subtract (keeping only positive counts)
Counter({'a': 2})
>>> c & d                       # intersection:  min(c[x], d[x]) # doctest: +SKIP
Counter({'a': 1, 'b': 1})
>>> c | d                       # union:  max(c[x], d[x])
Counter({'a': 3, 'b': 2})



>>>c = Counter('abb')
>>>c.update('a')
Counter({'a': 2, 'b': 2})
