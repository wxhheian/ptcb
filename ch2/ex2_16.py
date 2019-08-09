#你要一些 长字符串，想以指定的列宽将他们重新格式化
import os
import textwrap


def reformat_width():
    s = "Look into my eyes, look into my eyes, the eyes, the eyes,\
the eyes, not around the eyes, don't look around the eyes,\
look into my eyes, you're under."
    print(s)
    print('************************')
    print(textwrap.fill(s,70))     #等价于"\n".join(wrap(text, ...))
    print('************************')
    print(textwrap.fill(s,40))
    print('************************')
    print(textwrap.fill(s,40,initial_indent='    '))
    print("************************")
    print(textwrap.fill(s,40,subsequent_indent='    '))

    ##希望打印结果自动匹配终端大小
    print(os.get_terminal_size())
    print(os.get_terminal_size().columns)

    ##更多参考textwrap.TextWrapper文档

if __name__ == '__main__':
    reformat_width()
