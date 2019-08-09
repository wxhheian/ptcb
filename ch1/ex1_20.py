#现在有多个字典或者映射，你想将它们合并成一个单一的映射
from collections import ChainMap
def combine_map():
    a = {'x':1,'z':3}
    b = {'y':2,'z':4}
    c = ChainMap(a,b)
    print(c['x'])
    print(c['y'])
    print(c['z'])    # Output 3 (from a)   可见字典并不是真正和并在了一起,如果出现重复键，那么第一次出现映射值会被返回
    #大部分字典的常规操作对ChainMap()都适用
    print(len(c))
    print(list(c.keys()))
    print(list(c.values()))

    #对字典c的更新和删除操作总是影响的是列表中的第一个字典
    c['z'] = 10
    c['w'] = 40
    del c['x']
    print(a)
    #del c['y']   #报错：key not found in the first mapping

    values = ChainMap()
    values['x'] = 1
    ##Add a new mapping
    values = values.new_child()
    values['x'] = 2
    ##Add a new mapping
    values = values.new_child()
    values['x'] = 3
    print(values)
    print(values['x'])

    #discard the last mapping   最后一个
    values = values.parents
    print(values['x'])

    #discard last mapping  最后一个
    values = values.parents
    print(values['x'])
    print(values)








if __name__ == '__main__':
    combine_map()
