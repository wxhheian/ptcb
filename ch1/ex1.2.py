##*用来多个变量的传递
def drop_first_last(grades):             #去除第一个和最后一个分数，然后求平均
    first,*middle,last = grades
    return avg(middle)

>>>record=('Dave','dave@example.com','773-555-1212','847-555-1212')
>>>name,email.*phone_number=record
>>>name
'Dave'
>>>email
'dave@example.com'
>>>phone_number
['773-555-1212','847-555-1212']                ##利用嗯这种方法解压出来的变量永远是列表类型
>>>

#你有公司前8个月的销售数据，现想比较一下最近一个月数据与前面7个月的平均值对比

*trailing_qtrs,current_qtr = sales_record
trailing_avg = sum(trailing_qtrs)/len(trailing_qtrs)
return avg_comparison(trailing_avg,current_qtr)

>>>*trailing,current = [10,8,7,1,9,5,10,3]
>>>trailing
[10,8,7,1,9,5,10]
>>>current
3

##*表达式在迭代元素为可变长元组的序列时是很有用的，例如下面的带标签的元组序列
records = [
    ('foo',1,2),
    ('bar','hello'),
    ('foo',3,4)
]

def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar',s)

for tag,*args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
#输出结果
foo 1 2
bar hello
foo 3 4
#################

#*表达式在字符串分割的作用
>>> line = 'noboey:*:-2:-2:unprivileged user:/var/empty:/usr/bin/false'
>>> uname,*fields,homedir,sh = line.split(':')
>>>uname
'noboey'
>>>homedir
/var/empty
>>>sh
/usr/bin/false
>>>

###*表达式用在废弃的变量
>>> record=('acme',50,123.45,(12,18,2012))
>>> name,*_,(*_,year)=record
>>> name
'acme'
>>> year
2012
>>>

##*表达式实现递归算法
items = [1,10,7,4,5,9]

def sum(items):
    head,*tail =items
    return head + sum(tail) if tail else head

print(sum(items))
#输出结果
36
