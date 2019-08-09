#在两个字典中寻找相同点（比如相同的键，相同的值）

a = {
    'x':1,
    'y':2,
    'z':3
}

b = {
    'w':10,
    'x':11,
    'y':2
}


>>> a.keys() & b.keys()              #find keys in common
{'x', 'y'}
>>> a.keys() - b.keys()            #find keys in a that not in b
{'z'}
>>> a.items() & b.items()          #find (key,value) pairs in common
{('y', 2)}

>>> c = {key:a[key] for key in a.keys() - {'z','w'}}           #make a new dict with certan keys removed
>>> c
{'x': 1, 'y': 2}
>>>
