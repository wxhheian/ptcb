#heapq(Heap queue algorithm)库
#####nlargest(n,iterable) 取前n个最大的；  nsmallest(nmiterable)取前n个最小的
#eg1
import heapq
nums = [1,23,32,45,67,21,78,12]
print('3 largest',heapq.nlargest(3,nums))
print('3 smallest',heapq.nsmallest(3,nums))

#eg2
#nlargest(n,dicts,key)按照key取前n个最大的，nsmallest(n,dicts,key)按照key取前n个最小的
dicts=[
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

print('2 largest',heapq.nlargest(2,dicts,key= lambda s:s['price']))
print('2 largest',heapq.nsmallest(2,dicts,key= lambda s:s['price']))

#eg3
#heapify(x)  #将list x 转换为堆
#堆  参见http://www.imooc.com/article/273703
print('heap before',nums)
heapq.heapify(nums)
print('heap after',nums)

#eg4
#heappush(heap,item)   往堆里push一个元素
heapq.heappush(nums,10)
print('push 10',nums)

#eg5
#heappop(heap)   #从堆中pop一个最小的值，并从堆中移除，如果heap为空，为异常IndexError
smallest = heapq.heappop(nums)
print(smallest)
print('pop after',nums)
#smallest = heapq.heappop([])

#eg6
#heappushpop(heap,item)   push一个元素，然后pop一个最小的元素
smallest = heapq.heappushpop(nums,100)
print(smallest,nums)

#eg7
#heapreplace(heap,item)  #先pop最小的值，然后push item,若heap为空，则IndexError
heapq.heapreplace(nums,1)
print(nums)

#eg8
#merge(*iterables,key=None,reverse=False)  合并多个集合，返回堆排序后的数据，类型为iterator
newheap = heapq.merge(nums,[10,11,23])
print(newheap)
for item in newheap:
    print(item)
