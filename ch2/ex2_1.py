#你需要将一个字符串分割成多个字段，但分割符号（包括空格）不是固定的
#string对象的split()方法只适用于简单的字符串分割，它不允许有多个分割符
#re.split()分割字符串适用不同的分割符号

#正则表达式分割字符窗
import re
def split_str():
     line = 'asdf fjdk; afed,    fjek,asdf, foo'
     print(re.split(r'[;\s,]\s*',line))
     print(re.split(r'(;|,|\s)\s*',line))           #正则表达式如果使用了（）捕获分组，那么被匹配到的文本也将出现在结果列表中
     fields = re.split(r'(;|,|\s)\s*',line)
     values = fields[::2]
     delimiter = fields[1::2] + ['']
     print(''.join(v+d for v,d in zip(values,delimiter)))
     print(re.split(r'(?:,|;|\s)\s*',line))




if __name__ == '__main__':
    split_str()
