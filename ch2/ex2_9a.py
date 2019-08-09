import unicodedata
s1 = 'Spicy Jalape\u00f1o'
print(s1)
t1 = unicodedata.normalize('NFD',s1)
print(t1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))     #清除文本上面的一些变音符


for c in t1:
    print(not unicodedata.combining(c))


输出结果：
Spicy Jalapeño
Spicy Jalapeño
Spicy Jalapeno
True
True
True
True
True
True
True
True
True
True
True
True
True
False
True
