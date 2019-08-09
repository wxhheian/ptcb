#有一个数列，利用一些规则从中提取出需要的值或者缩短序列
##使用列表推导   ，用 [ ]
>>> mylist = [1,4,-5,10,-7,2,3,-1]
>>> [n for n in mylist if n > 0]
[1, 4, 10, 2, 3]
>>> [n for n in mylist if n < 0]
[-5, -7, -1]
>>> mylist1 = (1,4,-5,10,-7,2,3,-1)
>>> [n for n in mylist1 if n < 0]
[-5, -7, -1]

##使用生成器表达式迭代产生过滤元素   ，用（ ）
>>> (n for n in mylist1 if n < 0)
<generator object <genexpr> at 0x7f1ae59b1990>
>>> pos = (n for n in mylist if n > 0)
>>> pos
<generator object <genexpr> at 0x7f1ae59b1a98>
>>> for x in pos:
...     print(x)
...
1
4
10
2
3


>>> mylist = [1,4,-5,10,7,2,3,-1]
>>> mylist = [1,4,-5,10,-7,2,3,-1]
>>> import math
>>> [math.sqrt(n) for n in mylist if n >0]
[1.0, 2.0, 3.1622776601683795, 1.4142135623730951, 1.7320508075688772]
>>> clip_neg = [n if n >0 else 0 for n in mylist]
>>> clip_neg
[1, 4, 0, 10, 0, 2, 3, 0]
>>> clip_pos = [n if n<0 else 0 for n in mylist]
>>> clip_pos
[0, 0, -5, 0, -7, 0, 0, -1]
>>>
