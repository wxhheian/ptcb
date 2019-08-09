##operator.itemgetter()
>>> from operator import itemgetter
>>> a = [1,2,3]
>>> b = itemgetter(1)     #定义函数b,获取对象的第1个域的值
>>> b(a)
2
>>> b = itemgetter(1,0)   #定义函数b, 获取对象的第1个域和第0个域的值
>>> b(a)
(2, 1)

#要注意，operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值
>>> a = [('john','A',15),('jane','B',12),('dave','B',10)]

#sorted函数用来排序，sorted(iterable[, cmp[, key[, reverse]]])
#其中key的参数为一个函数或者lambda函数。所以itemgetter可以用来当key的参数
>>> sorted(a,key=itemgetter(1,2))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
>>> sorted(a,key=itemgetter(2))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
>>> sorted(a,key=itemgetter(1))
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
>>> sorted(a,key=itemgetter(0))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
>>> sorted(a,key=itemgetter(1,2))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
>>>
