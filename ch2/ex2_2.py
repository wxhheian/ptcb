#通过指定的文本模式去检查字符串的开头或结尾
import os
from urllib.request import urlopen
import re
def str_start():
    filename = 'spam.txt'                     #检查字符串开头或结尾使用str.startswith()   str.endswith()
    print(filename.endswith('.txt'))
    print(filename.startswith('file:'))
    url = 'http://www.python.org'
    print(url.startswith('http:'))

    #filenames = os.listdir('.')                 #当前目录下的文件
    filenames = os.listdir('/home/wxhheian/ptcb/ch1')
    print(filenames)
    #检查多种匹配可能，只需要将匹配项放到一个元组中去
    fil = [name for name in filenames if name.endswith(('a.py','.txt'))]
    print(fil)
    print(any(name.endswith('.py') for name in filenames))

def read_data(name):
    if name.startswith(('http:','https:','ftp:')):               ##startswith() 若有多个参数，必须以元组的形式
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

def str_slice():
    filename = 'spam.txt'
    print(filename[-4:] == '.txt')
    url = 'http://www.python.org'
    print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')

def str_re():
    url = 'http://www.python.org'
    rer = re.match('http:|https:|ftp:',url)
    print(rer)


# choices = ['http:','ftp:']
# url = 'http://www.python.org'
#url.startswith(choices)                #报错，startswith first arg must be str or a tuple of str
#url.startswith(tuple(choices))     #可以

#检查某个文件夹是否有指定的某个文件
#if any(name.endswith(('.py','.txt')) for name in listdir(dirname))




if __name__ == '__main__':
    str_start()
    str_slice()
    str_re()
