#字符串的搜索和替换
import re
from calendar import month_abbr

def change_date(m):             #change_date是一个替换模式，m是一个match object
     mon_name = month_abbr[int(m.group(1))]
     return '{} {} {}'.format(m.group(2),mon_name,m.group(3))

def search_replace():
    text = 'yeah, but no, but yeah, but no, but yeah'
    text_rep = text.replace('yeah','yep')
    print(text_rep)

    text1 = 'Today is 11/27/2012. PyCon starts 3/13/2013'
    text1_sub = re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text1)     #sub()第一个参数是被匹配的模式，第二个参数是替换模式，反斜杠数字比如\3指向前面模式的捕获组号
    print(text1_sub)

    ##采用编译提升性能
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    text1_pat = datepat.sub(r'\3-\1-\2',text1)
    print(text1_pat)

    #使用函数来替换
    text1_func = datepat.sub(change_date,text1)
    print(text1_func)

    #想知道有多少替换发生
    newtext,n = datepat.subn(r'\3-\1-\2',text1)
    print(newtext)
    print(n)





if __name__ == '__main__':
    search_replace()
