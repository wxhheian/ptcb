#用正则表达式去匹配多行文字

import re
def multiline_match():
    comment = re.compile(r'/\*(.*?)\*/')
    text1 = '/* this is a comment */'
    text2 = '''/* this is a
    multiline comment */
    '''
    result1 = comment.findall(text1)
    result2 = comment.findall(text2)
    print(result1)    #Output:[' this is a comment ']
    print(result2)   #Output: []

    #修改模式，增加对换行的支持
    comment1 = re.compile(r'/\*((?:.|\n)*?)\*/')
    result3 = comment1.findall(text2)
    print(result3)   #Output:[' this is a\n    multiline comment ']

    comment2 = re.compile(r'/\*((?:.|\n)*?)\*/',re.DOTALL)    #标志参数re.DOTLL
    result4 = comment2.findall(text2)
    print(result4)



if __name__ == '__main__':
    multiline_match()
