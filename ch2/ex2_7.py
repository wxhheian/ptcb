##用正则表达式匹配某个文本，但是找到的模式的最长可能匹配。而你想修改它为查找最短的可能匹配
import re
def shortest_match():
    str_pat = re.compile(r'\"(.*)\"')                 # 正则表达式中*是贪婪的
    text1 = 'Computer says "no."'
    str_find1 = str_pat.findall(text1)
    print(str_find1)
    text2 = 'Computer says "no." Phone says "yes."'
    str_find2 = str_pat.findall(text2)
    print(str_find2)        #Output:['no." Phone says "yes.']

    #修正贪婪的问题
    str_pat1 = re.compile(r'\"(.*?)\"')   #对它前面的正则式匹配0到1次重复。 ab? 会匹配 'a' 或者 'ab'。
    str_find3 = str_pat1.findall(text2)
    print(str_find3)  #Output:['no.', 'yes.']





if __name__ == '__main__':
    shortest_match()
