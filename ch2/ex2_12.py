#str的translate（）方法清理文本
import unicodedata
import sys

def clean_spaces(s):
    s = s.replace('\r',' ')
    s = s.replace('\t',' ')
    s= s.replace('\f',' ')
    return s



def translate_str():
    s = 'pýtĥöñ\fis\tawesome\r\n'
    print(s)

    #创建转换表格,再使用translate()方法
    remap = {
        ord('\t'):' ',
        ord('\f'):' ',
        ord('\r'):None
    }
    a = s.translate(remap)
    print(a)


    ##删除和音符
    cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))         ##参考ex2_9a.py
    b = unicodedata.normalize('NFD',a)
    print(b)
    print(b.translate(cmb_chrs))

    #unicode数字字符映射到ascii字符
    digitmap = { c: ord('0') + unicodedata.digit(chr(c)) for c in range(sys.maxunicode) if unicodedata.category(chr(c)) == 'Nd' }
    print(len(digitmap))
    #Arabic digits
    x = '\u0661\u0662\u0663'
    print(x.translate(digitmap))

    #unicodedata.category(chr)   返回分配给字符 chr 的常规类别为字符串。
    #unicodedata.digit(chr)  返回分配给字符 chr 的数字值作为整数。 如果没有定义这样的值，则返回 default ，如果没有给出，则 ValueError 被引发。


    ## 先标准化，然后使用encode和decode函数
    b = unicodedata.normalize('NFD',a)
    print(b.encode('ascii','ignore').decode('ascii'))    #ascii编码，解码操作丢弃了那些和音符，只在目标是获取文本对应ascii表示的时候生效





if __name__ == '__main__':
    translate_str()
