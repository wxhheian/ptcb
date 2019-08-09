>>> a = {'x':1,'z':3}
>>> b={'y':2,'z':4}
>>> dict(b)
{'y': 2, 'z': 4}
>>> type(dict(b))
<class 'dict'>
>>> type(b)
<class 'dict'>
>>> merged = dict(b)
>>> merged.update(a)
>>> merged
{'y': 2, 'z': 3, 'x': 1}
>>> a['x'] = 13                 #使用update()  对原字典进行修改并不会体现在合并字典里面
>>> merged['x']
1
>>>




>>> a = {'x':1,'z':3}
>>>
>>> b={'y':2,'z':4}
>>>
>>> merged = ChainMap(a,b)
>>> merged['x']
1
>>> a['x'] =42
>>> merged['x']                   #使用ChainMap()  对原字典进行修改会体现在合并字典里
42
>>>
