#使用unix Shell 中的通配符去匹配文本字符串
from fnmatch import fnmatch,fnmatchcase
def unix_match():
    print(fnmatch('foo.txt','*.txt'))
    print(fnmatch('foo.txt','?oo.txt'))
    print(fnmatch('Dat45.csv','Dat[0-9]*'))
    names = ['Dat1.csv','Dat2.csv','config.ini','foo.py']
    fmatch = [name for name in names if fnmatch(name,'Dat*.csv')]
    print(fmatch)

    ##fnmatch() 在unix上区分大小写
    print(fnmatch('foo.txt','*.TXT'))     #False on Unix  but True on Windows
    ##fnmatchcase() 在Unix和Windows都区分大小写
    print(fnmatchcase('foo.txt','*.TXT'))

    # 处理普通文本
    addresses = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1039 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY',
        ]
    print([addr for addr in addresses if fnmatchcase(addr,'*ST')])
    print([addr for addr in addresses if fnmatchcase(addr,'54[0-9][0-9]*CLARK*')])



if __name__ == '__main__':
    unix_match()
