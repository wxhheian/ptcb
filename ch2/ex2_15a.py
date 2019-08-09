import sys

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))
    #return text.format_map(safesub(sys._getframe(0).f_locals))   #查看结果如何

#sys._getframe([depth])
#Return a frame object from the call stack.
#If optional integer depth is given, return the frame object that many calls below the top of the stack.
#If that is deeper than the call stack, ValueError is raised. The default for depth is zero, returning the frame at the top of the call stack.

class safesub(dict):
    """防止key找不到"""
    def __missing__(self,key):
        return '{' + key + '}'

name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages'))
print(sub('Your favorite color is {color}'))
