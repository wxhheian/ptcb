# %r 与{!r} 在python里都是转义字符
>>> a = '123'
>>> b = 'hello, {!r}'.format(a)
>>> b
"hello, '123'"

>>> a = '123'
>>> b = 'hello, %r' % a
>>> b
"hello, '123'"

>> b = 'hello, !r' % '123'                               #  ！只在format中运用
 Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 TypeError: not all arguments converted during string formatting


>>>a=[(-5,0),(-4,0)]
>>>heapq.heappush(a,(-6,0))
>>>a
[(-6,0),(-5,0),(-4,0)]
>>>heapq.heappop(a)
(-6,0)


>>> a=[(-5,0),(-5,1)]
>>> heapq.heappop(a)
(-5, 0)
