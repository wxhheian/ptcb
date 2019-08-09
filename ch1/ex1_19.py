#你需要在数据序列上执行聚集函数（比如sum(),min(),max()）,但是首先需要转换或者过滤数据.转换并聚集函数
import os
def trans_reduce():
    nums = [1,2,3,4,5]
    s1 = sum(x * x for x in nums)            #迭代器经过sum()后是一个数，使用迭代器可以不用多加（）
    print(s1)
    s2 = sum((x * x for x in nums))       #s1与s2结果一样，相比下，s1表达式更加优雅
    s3  = sum([x * x for x in nums])            #不是用迭代器，必须加（）
    print(s2)
    print(s3)

    path = '/home/wxhheian/ptcb/ch1'
    files = os.listdir(path)
    if any(name.endswith('.py') for name in files):
        print('There be python')
    else:
        print('Sorry,no python')

    #Output a tuple a CSV
    s = ('ACME',50,123.45)
    print(','.join(str(x) for x in s))

    #Data reduction across fields of a data structure
    portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
    ]
    min_shares1 = min(a['shares'] for a in portfolio)
    print(min_shares1)
    min_shares2 = min(s['shares'] for s in portfolio)
    min_shares3 = min(portfolio,key=lambda s:s['shares'])
    print(min_shares2)
    print(min_shares3)



if __name__ =='__main__':
    trans_reduce()
