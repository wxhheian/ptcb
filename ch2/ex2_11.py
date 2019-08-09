#删除字符串中的不需要的字符
import re
def str_strip():
    ##strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列,不会对中间的字符串产生影响。lstrip()从左边开始执行，rstrip()从右边开始执行
    s = '  hello world \n'
    print(s.strip())
    print(s.lstrip())
    print(s.rstrip())

    #指定删除字符
    t = '----hello======'
    print(t.lstrip('-'))
    print(t.rstrip('='))
    print(t.strip('-='))

    ##strip()方法不会对中间的文本产生影响
    s = ' hello       world \n'
    s = s.strip()
    print(s)

    #想要处理中间的空格，可以使用replace()或者re.sub()
    print(s.replace(' ',''))     #Output:'helloworld'
    print(re.sub('\s+',' ',s))    #Output:'hello world'


    #生成器表达式用于文件中读取多行数据
    with open(filename) as f:
        lines = (line.strip() for line in f)
        for line in lines:
            print(line)



if __name__ == '__main__':
    str_strip()
