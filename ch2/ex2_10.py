#你在使用正则表达式处理文本，但关注的是Unicode字符处理，在正则表达是中使用Unicode

import re
def re_unicode():
    num = re.compile('\d+')   #匹配任何Unicode十进制数（就是在Unicode字符目录[Nd]里的字符）。这包括了 [0-9] ，和很多其他的数字字符。如果设置了 ASCII 标志，就只匹配 [0-9] 。
    #ASCII digits
    print(num.match('123'))
    #Arabic digits
    print(num.match('\u0661\u0662\u0663'))
    arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
    pat = re.compile('stra\u00dfe',re.IGNORECASE)           #大小写忽略
    s = 'straße'
    print(pat.match(s))    #Match
    print(pat.match(s.upper()))  #Doesn't match
    print(s.upper())     #Output:'STRASSE'


if __name__ == '__main__':
    re_unicode()
