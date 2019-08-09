#处理html或者xml
import html
from html.parser import HTMLParser
from xml.sax.saxutils import unescape
def html_xml():
    #替换文本字符串中的‘<’或者‘>’,使用html.escape()
    s = 'Elements are written as "<tag>text</tag>"'
    print(s)
    print(html.escape(s))

    #Disable eacaping of quotes
    print(html.escape(s,quote=False))

    s = 'Spicy Jalapeño'
    print(s.encode('ascii',errors='xmlcharrefreplace'))

    #为了替换文本中的编码实体，且你在处理HTML或者XML文本，试着先使用一个合适的HTML或者XML解析器，通常情况下，这些工具会自动替你替换这些编码值
    #有些时候却是有一些编码值的原始文本
    s = 'Spicy &quot;Jalape&#241;o&quot.'
    p = HTMLParser()
    print(p.unescape(s))
    t = 'The pompt is &gt;&gt;&gt;'
    print(unescape(t))



if __name__ == '__main__':
    html_xml()
