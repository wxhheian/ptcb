#通过某种方式来格式化字符串（比如对齐字符串）

def align_str():
    text = 'Hello World'
    textl = text.ljust(20)  # ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串
    textr = text.rjust(20)
    textc = text.center(20)
    print(textl)
    print(textr)
    print(textc)

    #接受一个可选择的填充字符
    textr_pull = text.rjust(20,'=')
    print(textr_pull)
    textc_pull = text.center(20,'*')
    print(textc_pull)

    #format()同样也可以对齐字符串，使用> < ^后紧跟一个指定宽度 ,若要指定一个非空格填充字符，将它写到对齐字符的前面即可
    textr_format = format(text,'>20')
    textl_format = format(text,'<20')
    textc_format = format(text,'^20')
    print(textr_format)
    print(textl_format)
    print(textc_format)
    textr_format_pull = format(text,'*>20s')
    print(textr_format_pull)

    ##格式化多个字符
    text_mulformat = '{:>10s} {:>10s}'.format('Hello','World')      #注意'{=>10s} {=>10s}'.format('Hello','World') 报错
    print(text_mulformat)

    ##格式化数字
    x = 1.2345
    print(format(x,'>10'))
    print(format(x,'^10.2f'))


if __name__  == '__main__':
    align_str()
