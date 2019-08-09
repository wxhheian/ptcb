#你有一个字典列表，通过某个关键字来排序这个列表
from operator import itemgetter

def sort_dictlist():
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

    rows_by_fname = sorted(rows,key=itemgetter('fname'))
    rows_by_lname = sorted(rows,key=itemgetter('lname'))
    print(rows_by_fname)
    print(rows_by_lname)

    rows_by_lfname = sorted(rows,key=itemgetter('lname','fname'))
    print(rows_by_lfname)

##  rows_by_fname = sorted(rows,key=lambda r:r['fname'])     #与12行代码效果相同
##  rows_by_lname = sorted(rows,key=lambda r:r['lname'])      #与13行代码效果相同

    minrow = min(rows,key=itemgetter('uid'))
    maxrow = max(rows,key=itemgetter('uid'))
    print(minrow)
    print(maxrow)

if __name__ == '__main__':
    sort_dictlist()
