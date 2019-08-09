#怎么样在一个序列上保持元素的顺序同时消除重复值
def dedupe(items):               ##只适用于序列上的值都是hashable
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

>>>a = [1,5,2,1,9,1,5,10]
>>> dedupe(a)
<generator object dedupe at 0x7ff03aa38f10>
>>> list(dedupe(a))
[1, 5, 2, 9, 10]
>>>


############################   要消除元素不可hashable,比如dict类型
def dedupe(items,key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)          #注意这里的key(item)        
        if val not in seen:
            yield item
            seen.add(val)


>>>a = [{'x':1,'y':2},{'x':1,'y':3},{'x':1,'y':2},{'x':2,'y':4}]
>>> dedupe(a,key=lambda d:(d['x'],d['y']))
<generator object dedupe at 0x7f9328247e08>
>>> list(dedupe(a,key=lambda d:(d['x'],d['y'])))
[{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
>>> list(dedupe(a,key=lambda d:(d['x'])))
[{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
>>> list(dedupe(a,key=lambda d:(d['y'])))
[{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
>>>

########################################################

# def dedupe(items,key=None):
#     for item in items:
#         val = item if key is None else key(item)          #if key is None , val = item
#         print(val)                                             #if key is not None ,val = key(item)
#
# a = [{'x':1,'y':2},{'x':1,'y':3},{'x':1,'y':2},{'x':2,'y':4}]
# >>> dedupe(a,key=None)
# {'x': 1, 'y': 2}
# {'x': 1, 'y': 3}
# {'x': 1, 'y': 2}
# {'x': 2, 'y': 4}
# >>> dedupe(a,key=lambda d:(d['x'],d['y']))
# (1, 2)
# (1, 3)
# (1, 2)
# (2, 4)
