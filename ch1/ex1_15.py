#你有一个字典或者实例的序列，然后你想根据某个特征的字段比如date来分组迭代访问
#分组迭代  根据某一列的内容分为不同的维度进行拆解，将同一维度的再进行聚合
from operator import itemgetter
from itertools import groupby
def group_iter():
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

    #sort by the desired field first
    #sorted(rows,key=itemgetter('date'))      #不能用18行代码,没有改变rows
    rows.sort(key=itemgetter('date'))
    ##Iterate in groups
    for date,items in groupby(rows,key=itemgetter('date')):
        print(date)
        for i in items:
            print('',i)

if __name__ == '__main__':
    group_iter()

#>>> list(groupby(rows,key=itemgetter('date')))
#[('07/01/2012', <itertools._grouper object at 0x7fa8dffa7908>), ('07/02/2012', <itertools._grouper object at 0x7fa8dffa7940>), ('07/03/2012', <itertools._grouper object at 0x7fa8dffa7978>), ('07/04/2012', <itertools._grouper object at 0x7fa8dffa79b0>)]
