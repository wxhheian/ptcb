#忽视大小写的方式搜索与替换文本字符串

import re

def matchcase(word):
    def replace(m):             #m为一个match object
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


def case_insentivity():
    text = 'UPPER PYTHON, lower python, Mixed Python'
    text_insentivity_find = re.findall('python',text,flags=re.IGNORECASE)    #忽视大小写
    print(text_insentivity_find)
    text_insentivity_sub = re.sub('python','snake',text,flags=re.IGNORECASE)       #替换字符并不会自动跟被匹配字符串的大小保持一致
    print(text_insentivity_sub)   #Output:UPPER snake, lower snake, Mixed snake

    #使用函数
    text_insentivity_func = re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE)
    print(text_insentivity_func)

    ##matchcase('snake')返回一个回调函数（参数必须是match对象),sub()函数除了接受替换字符串外，还能接受一个回调函数,表示替换模式
    ##和ex2_5的change_date比较  ！！！！！！！！！





if __name__ == '__main__':
    case_insentivity()
