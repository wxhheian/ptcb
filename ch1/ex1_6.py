##实现一个键对应多个值的字典
#####实现方法一：将多个值放到不同的容器中
# d = {
#     'a':[1,2,3],
#     'b':[4,5]
# }
# e = {
#    'a':{1,2,3},
#    'b':{4，5}
# }

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)
d['b'].append(4)

e = defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e['b'].add(4)

################setdefault
f={}
f.setdefault('a',[]).append(1)
f.setdefault('a',[]).append(2)
