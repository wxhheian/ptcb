#匹配或搜索特定模式的文本
import re

def match_search():

    text = 'yeah, but no, but yea,but no, but yeah'
    #exact match
    print(text == 'yeah')
    #match at start or end
    print(text.startswith('yeah'))
    print(text.endswith('no'))
    print(text.find('no'))       #第一次find 'no'


    text1 = '11/27/2012'
    text2 = 'Nov 27, 2012'

    #simple match: \d+ means match one or more digits
    if re.match(r'\d+/\d+/\d+',text1):
        print('yes')
    else:
        print('no')

    if re.match(r'\d+/\d+/\d+',text2):
        print('yes')
    else:
        print('no')

    #如果你想用同一个模式去匹配，应该先将模式字符串预编译为模式对象
    datepat = re.compile(r'\d+/\d+/\d+')
    if datepat.match(text1):
        print('yes')
    else:
        print('no')

    if datepat.match(text2):
        print('yes')
    else:
        print('no')


    #match总是从字符串开始的位置去匹配(若开头就不匹配，则报错)，若想查找字符串任意位置的模式，使用findall()

    text3 = 'Today ia 11/27/2012. PyCon starts 3/13/2013'
    print(datepat.findall(text3))

    #定义正则表达式的时候，利用括号去捕获分组
    datepat1 = re.compile(r'(\d+)/(\d+)/(\d+)')     #加r 则不去解析反斜杠     #等价于 re.compile('(\\d+)/(\\d+)/(\\d+)')
    m = datepat1.match('11/27/2012')
    print(m)
    #extract the content of each group
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
    print(m.groups())
    month,day,year = m.groups()               #这里是groups()
    print(datepat1.findall(text3))
    for month,day,year in datepat1.findall(text3):
        print('{}-{}-{}'.format(year,month,day))

    ##findall会以list方回所有匹配，若想以迭代的方式返回匹配，可以使用finditer()方法
    for m in datepat1.finditer(text3):
        print(m.groups())









if __name__ == '__main__':
    match_search()
