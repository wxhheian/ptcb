#集合（Set）是一个无序的不重复元素序列，使用大括号{ }或者set()创建集合，创建空集合必须使用set(),不能用{},应为{}用来创建空字典

>>> basket = {'apple','orange','apple','pear','orange','banana'}
>>> basket                              ##展示了去重功能
{'banana', 'orange', 'apple', 'pear'}

>>> a = set('abracadabra')
>>> b= set('alacazam')
>>> a
{'r', 'a', 'c', 'd', 'b'}
>>> b
{'a', 'm', 'z', 'l', 'c'}
>>> a - b                #在a中有，但b中没有
{'r', 'b', 'd'}
>>> a | b      #a或b
{'r', 'a', 'm', 'z', 'l', 'c', 'd', 'b'}
>>> a & b     #a and b
{'a', 'c'}
>>> a ^ b   # 不同时包含于a和b的元素
{'r', 'm', 'z', 'l', 'b', 'd'}

>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
>>>


>>>thisset = set(("Google", "Runoob", "Taobao"))
>>> thisset.add("Facebook")
>>> print(thisset)
{'Taobao', 'Facebook', 'Google', 'Runoob'}



>>>thisset = set(("Google", "Runoob", "Taobao"))
>>> thisset.update({1,3})
>>> print(thisset)
{1, 3, 'Google', 'Taobao', 'Runoob'}
>>> thisset.update([1,4],[5,6])
>>> print(thisset)
{1, 3, 4, 5, 6, 'Google', 'Taobao', 'Runoob'}
>>>


>>>thisset = set(("Google", "Runoob", "Taobao"))
>>> thisset.remove("Taobao")
>>> print(thisset)
{'Google', 'Runoob'}
>>> thisset.remove("Facebook")   # 不存在会发生错误
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Facebook'
>>>


##pop()  随机删除一个元素

thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
x = thisset.pop()

print(x)
输出结果:
Runoob



>>>thisset = set(("Google", "Runoob", "Taobao"))
>>> len(thisset)
3



>>>thisset = set(("Google", "Runoob", "Taobao"))
>>> thisset.clear()
>>> print(thisset)
set()
