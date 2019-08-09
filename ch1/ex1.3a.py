#deque对象，是一个新的双向队列对象，类似于list对象
#class collections.deque([iterable[,maxlen]])
#如果maxlen没有指定，则deques可以增加到任意长度，否则限定长度。当限定长度的deque满了，当新项加入时，同样数量的项就从另一端弹出
###################双向队列（deque）对象支持以下方法：#############
#append(x)   添加x到右端
#appendleft(x)  添加x到左端
#clear()         移除所有元素
#copy()    创建一份浅拷贝
#count(x)          #计算deque中x元素的个数
#extend(iterable)  #拓展deque的右侧，通过添加iterable参数中的元素
#extendleft(iterable)     #注意参数顺序被反过来添加
#index(x[,start[,stop]])      #返回第 x 个元素（从 start 开始计算，在 stop 之前）。返回第一个匹配，如果没找到的话，升起 ValueError 。
#insert(i,x)   #在位置i插入x
#pop() popleft()
#remove(value)  #移除找到的第一个value
#reversed()   #将deque逆序排列
#rotate(1)  #向右循环移动n步    rotate(1) #向左循环1步
#maxlen   #Deque的最大长度
###################################################

>>> from collections import deque
>>> d = deque('ghi')                 # make a new deque with three items
>>> for elem in d:                   # iterate over the deque's elements
...     print(elem.upper())
G
H
I

>>> d.append('j')                    # add a new entry to the right side
>>> d.appendleft('f')                # add a new entry to the left side
>>> d                                # show the representation of the deque
deque(['f', 'g', 'h', 'i', 'j'])

>>> d.pop()                          # return and remove the rightmost item
'j'
>>> d.popleft()                      # return and remove the leftmost item
'f'
>>> list(d)                          # list the contents of the deque
['g', 'h', 'i']
>>> d[0]                             # peek at leftmost item
'g'
>>> d[-1]                            # peek at rightmost item
'i'

>>> list(reversed(d))                # list the contents of a deque in reverse
['i', 'h', 'g']
>>> 'h' in d                         # search the deque
True
>>> d.extend('jkl')                  # add multiple elements at once
>>> d
deque(['g', 'h', 'i', 'j', 'k', 'l'])
>>> d.rotate(1)                      # right rotation
>>> d
deque(['l', 'g', 'h', 'i', 'j', 'k'])
>>> d.rotate(-1)                     # left rotation
>>> d
deque(['g', 'h', 'i', 'j', 'k', 'l'])

>>> deque(reversed(d))               # make a new deque in reverse order
deque(['l', 'k', 'j', 'i', 'h', 'g'])
>>> d.clear()                        # empty the deque
>>> d.pop()                          # cannot pop from an empty deque
Traceback (most recent call last):
    File "<pyshell#6>", line 1, in -toplevel-
        d.pop()
IndexError: pop from an empty deque

>>> d.extendleft('abc')              # extendleft() reverses the input order
>>> d
deque(['c', 'b', 'a'])

>>> new=deque(d,3)
>>> new
deque(['c', 'c', 1], maxlen=3)
>>> new.append('a')
>>> new
deque(['c', 1, 'a'], maxlen=3)


>>>q=deque(maxlen=3)  #创建一个长度为3的队列
