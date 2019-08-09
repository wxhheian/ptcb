import heapq
nums = [1,8,2,23,7,-4,18,23,42,37,2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

>>>nums = [1,8,2,23,7,-4,18,23,42,37,2]
>>>import heapq
>>>heap = list(nums)
[-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]

#heap[0]  永远是最小的书
#heapq.heappop(heap)  弹出最小的数


#sorted用法
>>>g=[1,4,6,8,9,3,5]
>>>sorted(g)
Out[30]: [1, 3, 4, 5, 6, 8, 9]

>>>sorted((1,4,8,9,3,6))
Out[33]: [1, 3, 4, 6, 8, 9]

>>>sorted('gafrtp')
Out[35]: ['a', 'f', 'g', 'p', 'r', 't']            #以上是顺序排列

>>>sorted((1,4,8,9,3,6),reverse=True)     #逆序排列

>>>l=[('a', 1), ('b', 2), ('c', 6), ('d', 4), ('e', 3)]
>>>sorted(l, key=lambda x:x[0])
Out[39]: [('a', 1), ('b', 2), ('c', 6), ('d', 4), ('e', 3)]
>>>sorted(l, key=lambda x:x[0], reverse=True)
Out[40]: [('e', 3), ('d', 4), ('c', 6), ('b', 2), ('a', 1)]
>>>sorted(l, key=lambda x:x[1])
Out[41]: [('a', 1), ('b', 2), ('e', 3), ('d', 4), ('c', 6)]
>>>sorted(l, key=lambda x:x[1], reverse=True)
Out[42]: [('c', 6), ('d', 4), ('e', 3), ('b', 2), ('a', 1)]
