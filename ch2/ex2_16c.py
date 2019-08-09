##形参*args 和 **kwargs

#*args：（表示的就是将实参中按照位置传值，多出来的值都给args，且以元祖的方式呈现）
def foo(x,*args):
    print(x)
    print(args)

foo(1,2,3,4,5)#其中的2,3,4,5都给了args
#Output:
# 1
# (2, 3, 4, 5)


##当*args，位置参数与默认参数混用的时候，注意使用顺序
#当顺序是位置参数，默认参数，*args时
def foo(x,y=1,*args):
    print(x)
    print(y)
    print(args)

foo(1,2,3,4,5)#其中的x为1，y=1的值被2重置了，3,4,5都给了args
#执行结果是：
# 1
# 2
# (3, 4, 5)

#当顺序是位置参数、*args、默认参数
def foo(x,*args,y=1):
    print(x)
    print(args)
    print(y)

foo(1,2,3,4,5)#其中的x为1，2,3,4,5都给了args,y按照默认参数依旧为1
#Output:
1
(2, 3, 4, 5)
1

####**kwargs：（表示的就是形参中按照关键字传值把多余的传值以字典的方式呈现）
def foo(x,**kwargs):
    print(x)
    print(kwargs)
foo(1,y=1,a=2,b=3,c=4)#将y=1,a=2,b=3,c=4以字典的方式给了kwargs
#Output:
1
{'y': 1, 'a': 2, 'b': 3, 'c': 4}


####位置参数、*args、**kwargs三者的顺序必须是位置参数、*args、**kwargs，不然就会报错：
def foo(x,*args,**kwargs):
    print(x)
    print(args)
    print(kwargs)
foo(1,2,3,4,y=1,a=2,b=3,c=4)#将1传给了x，将2,3,4以元组方式传给了args，y=1,a=2,b=3,c=4以字典的方式给了kwargs
#Output:
1
(2, 3, 4)
{'y': 1, 'a': 2, 'b': 3, 'c': 4}

#位置参数、默认参数、**kwargs三者的顺序必须是位置参数、默认参数、**kwargs，不然就会报错：
def foo(x,y=1,**kwargs):
    print(x)
    print(y)
    print(kwargs)
foo(1,a=2,b=3,c=4)#将1按照位置传值给x，y按照默认参数为1，a=2,b=3,c=4以字典的方式给了kwarg
#Output:
1
1
1
{'a': 2, 'b': 3, 'c': 4}
