>>>from collections import defaultdict
>>>s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
>>>d = defaultdict(list)
>>>for k, v in s:
...    d[k].append(v)

>>>d
defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})
>>>

>>> d = {}
>>> for k,v in s:
...     d.setdefault(k,[]).append(v)
...
>>> d
{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
>>>

###设置default_factory为int,使defaultdict在计数方面有很好的作用
>>> s = 'mississippi'
>>> d = defaultdict(int)
>>> for k in s:
...   d[k] += 1
...
>>> d
defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2})
>>>


>>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
>>> d= defaultdict(set)
>>> for k,v in s:
...     d[k].add(v)
...
>>>
>>> d
defaultdict(<class 'set'>, {'yellow': {1, 3}, 'blue': {2, 4}, 'red': {1}})
