##slice()
#slice(start,stop,step)

>>> myslice= slice(5)
>>> myslice
slice(None, 5, None)
>>> slice(4)
slice(None, 4, None)
>>> slice(1,4)
slice(1, 4, None)
>>> arr= range(10)
>>> arr
range(0, 10)
>>> list(arr)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> arr[myslice]
range(0, 5)
>>> list(arr[myslice])
[0, 1, 2, 3, 4]
>>>


>>> items = [0,1,2,3,4,5,6]
>>> a = slice(2,4)
>>> items[2:4]
[2, 3]
>>> items[a]
[2, 3]
>>> items[a] = [10,11]
>>> items
[0, 1, 10, 11, 4, 5, 6]
>>> del items[a]
>>> items
[0, 1, 4, 5, 6]


>>> a = slice(5,50,2)
>>> a.start
5
>>> a.stop
50
>>> a.step
2


>>> s = 'HelloWorld'
>>> a.indices(len(s))                   #缩小a的范围，以满足s的边界
(5, 10, 2)
