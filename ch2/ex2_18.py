#你有一个字符串，想从左至右解析为一个令牌流

import re
from collections import namedtuple

def tokenize_str():
    text = 'foo = 23 + 42 * 10'
    print(text)
    tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
              ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
    NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
    NUM = r'(?P<NUM>\d+)'
    PLUS = r'(?P<PLUS>\+)'
    TIMES = r'(?P<TIMES>\*)'
    EQ = r'(?P<EQ>=)'
    WS = r'(?P<WS>\s+)'
    master_pat = re.compile('|'.join([NAME,NUM,PLUS,TIMES,EQ,WS]))   #?P<TOKENNAME>用于给一个模式命名，以供后面使用



if __name__ == '__main__':
    tokenize_str()
