#Unicode（统一码、万国码、单一码）是计算机科学领域里的一项业界标准，包括字符集、编码方案等。
#Unicode 是为了解决传统的字符编码方案的局限而产生的，它为每种语言中的每个字符设定了统一并且唯一的二进制编码，以满足跨语言、跨平台进行文本转换、处理的要求。
#string对象的split()方法只适用于简单的字符串分割，它不允许有多个分割符
#Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
#str.split(str="", num=string.count(str)).
#str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
#num -- 分割次数。默认为 -1, 即分隔所有。


str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print(str.split( ));       # 以空格为分隔符，包含 \n
print(str.split(' ', 1 )); # 以空格为分隔符，分隔成两个

txt = "Google#Runoob#Taobao#Facebook"

# 第二个参数为 1，返回两个参数列表
x = txt.split("#", 1)

print(x)

##############################################################

##########正则表达式
#参考  https://docs.python.org/zh-cn/3.7/library/re.html
