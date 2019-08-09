###__repr__  用法
class Item:
    def __init__(self,name):
        self.name = name

print(Item('aaaa'))
输出结果：
<__main__.Item object at 0x7f74363c7978>

#########################

###__repr__控制打印类的时候，控制类输出的字符串
class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return 'Iiitem({!r})'.format(self.name)

输出结果：
Iiitem('aaaaa')
