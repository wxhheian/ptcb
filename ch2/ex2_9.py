#处理Unicode字符串，确保所有字符串在底层有相同的表示
#在Unicode中，某些字符能够用多个合法的编码表示
#Unicode字符串标准化表示
import unicodedata
def nor_unicode():
    s1 = 'Spicy Jalape\u00f1o'                    #\u表示unicode编码
    s2 = 'Spicy Jalapen\u0303o'
    print(s1,s2)
    print(s1 == s2)
    print(len(s1),len(s2))

    t1 = unicodedata.normalize('NFC',s1)   #normalize()第一个参数指定字符串标准化的方式
    t2 = unicodedata.normalize('NFC',s2)     #NFC表示字符应该是整体组成（比如可能的话就使用单一编码）
    print(t1==t2)
    print(ascii(t1))
    t3 = unicodedata.normalize('NFD',s1)    #NFD表示字符应该分解为多个组合字符表示
    t4 = unicodedata.normalize('NFD',s2)
    print(t3 == t4)
    print(ascii(t3))


    s = '\ufb01'  # A single character
    print(s, len(s))
    print(unicodedata.normalize('NFD', s), len(unicodedata.normalize('NFD', s)))
    print(unicodedata.normalize('NFKC', s), len(unicodedata.normalize('NFKC', s)))
    print(unicodedata.normalize('NFKD', s), len(unicodedata.normalize('NFKD', s)))

    t1 = unicodedata.normalize('NFD',s1)
    print(''.join(c for c in t1 if not unicodedata.combining(c)))     #清除文本上面的一些变音符

    ##combining()函数可以测试一个字符是否为和声字符  combining(chr)返回分配给字符 chr 的规范组合类作为整数。如果没有定义组合类，则返回 0 


if __name__ == '__main__':
    nor_unicode()
