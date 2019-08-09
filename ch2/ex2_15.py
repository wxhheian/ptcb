#字符串插入变量.想要创建一个内含变量的字符串
import sys

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))
    ##sub函数使用sys._getframe(1)返回调用者的柞帧，可以从中访问属性f_locals来获得局部变量

class Info:
    def __init__(self,name,n):
        self.name = name
        self.n = n


class safesub(dict):
    """防止key找不到"""
    def __missing__(self,key):
        return '{' + key + '}'

def var_string():
    s = '{name} has {n} messages.'
    print(s.format(name='Guido',n=37))

    ##利用变量域替换变量,format_map()和vars()
    name = 'Guido'
    n = 37
    print(s.format_map(vars()))

    ##vars()同样适用于对象实例
    a = Info('Guido',37)
    print(s.format_map(vars(a)))

    ##format和format_map()不能处理变量缺失的情况
    # s.format(name='Guido')  #  KeyError: 'n'

    ##为了避免这种缺失变量的情况，可以定义一个含有__missing__方法的字典safesub(dict)
    del n    #Make sure n is undefined
    print(s.format_map(safesub(vars())))    #Output:Guido has {n} messages.

    ##如果你发现子代码中频繁地执行这些步骤，可以将变量替换步骤用一个工具函数封装起来,用sub函数封装
    name = 'Guido'
    n = 37
    print(sub('Hello {name}'))
    print(sub('You have {n} messages'))
    print(sub('Your favorite color is {color}'))








if __name__ == '__main__':
    var_string()
