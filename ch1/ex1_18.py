#映射名称到序列元素,通过名称访问序列
#collections.namedtuple(),你需要传递一个类型名和你需要的字段给它，然后它会返回一个类，你可以初始化这个类
from collections import namedtuple
def name_seq():
    Subscriber = namedtuple('Subscriber',['addr','joined'])      #定义一个类
    sub = Subscriber('jonesy@example.com','2012-10-19')      #初始化这个类
    print(sub)
    print(sub.addr)            #打印属性
    print(sub.joined)
    #namedtuple支持所有的普通元组的操作
    print(len(sub))
    addr,joined = sub
    print(addr)
    print(joined)


   ##命名元组的一个主要用途是将你的代码从下标操作中解脱出来（若有一个很大的元组类表）
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

def compute_cost2(records):
    Stock = namedtuple('Stock',['name','shares','price'])
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total




Stock1 = namedtuple('Stock',['name','shares','price','date','time'])
#create a prototype instance
stock_prototype = Stock1('',0,0.0,None,None)

#function to convert a dictionary to a Stock1
def dict_to_stock(s):
    return stock_prototype._replace(**s)

def default_stock():
    a = {'name':'ACME','shares':100,'price':123.45}
    b = {'name':'ACME','shares':100,'price':123.45,'date':'12/17/2012'}
    print(dict_to_stock(a))
    print(dict_to_stock(b))





if __name__ == '__main__':
    name_seq()
    # rs = [('aa', 12, 33)]
    rs = [['aa', 12, 33]]  # 元组和序列都可以
    print(compute_cost(rs))
    print(compute_cost2(rs))
    Stock = namedtuple('Stock',['name','shares','price'])
    s = Stock('ACME',100,123.45)
    print(s)
    #s.shares = 75   #报错，命名元组是不能修改的
    s = s._replace(shares=75)
    print(s)
    default_stock()
