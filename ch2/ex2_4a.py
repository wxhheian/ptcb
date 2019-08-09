#str.find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
#str.find(str, beg=0, end=len(string))

#     str -- 指定检索的字符串
#     beg -- 开始索引，默认为0。
#     end -- 结束索引，默认为字符串的长度。
# 如果包含子字符串返回开始的索引值，否则返回-1。
str1 = "this is string example....wow!!!";
str2 = "exam";

print(str1.find(str2))
print(str1.find(str2, 10))
print(str1.find(str2, 40))


##python中的字符串 加r 与不加r的区别： 防止转义     由于正则表达式和 \ 会有冲突，因此，当一个字符串使用了正则表达式后，最好在前面加上'r'。
s=r'\tt'
print(s)
#Output:'\tt‘
s='\tt'
print(s)
#Output:'        t'


######
#re.match是用来进行正则匹配检查的方法，若字符串匹配正则表达式，则match方法返回匹配对象（Match Object），否则返回None（注意不是空字符串""）。
#匹配对象Macth Object具有group方法，用来返回字符串的匹配部分。
# 01：“.”匹配任意1个字符
result=re.match(".....","baaop")
a=result.group()
print(a)
#结果：baaop

# 02:“[]”匹配[]中列举的字符
# 字符串第一个字符只要存在于[]中就能成功匹配，
# [a-zA-Z0-9_]表示可以匹配"a-z","A-Z","0-9"和"_"区间内的所有元素
result=re.match("[Aa]","Aaaaaaabbba")
a=result.group()
print(a)
#结果：A


############
>>> datepat1 = re.compile(r'(\d+)/(\d+)/(\d+)')
>>> m = datepat1.match('11/27/2012abcdef')
>>> m.groups()
('11', '27', '2012')
>>> m.group()
'11/27/2012'
>>> m.group(0)
'11/27/2012'
>>> m.group(1)
'11'
>>> m.group(2)
'27'
>>> m.group(3)
'2012'
>>>

####re中 $匹配字符串的末尾,以达到精确匹配的效果
>>> datepat1 = re.compile(r'(\d+)/(\d+)/(\d+)$')
>>> datepat1.match('11/27/2012abacdg')
>>> m = datepat1.match('11/27/2012abacdg')
>>> m.gruop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'gruop'
>>> datepat2 = re.compile(r'(\d+)/(\d+)/(\d+)')
>>> c = datepat2.match('11/27/2012abcdef')
>>> c
<_sre.SRE_Match object; span=(0, 10), match='11/27/2012'>
>>> c.group()
'11/27/2012'

>>>text3 = 'Today ia 11/27/2012. PyCon starts 3/13/2013'
>>>re.findall(r'(\d+)/(\d+)/(\d+)',text3)
[('11', '27', '2012'), ('3', '13', '2013')]
