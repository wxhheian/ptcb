#os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中。
#只支持在 Unix, Windows 下使用。
#os.listdir(path)

import os
path = '/home/wxhheian/ptcb/ch1'
files = os.listdir(path)
print(files)
for file in files:
    print(file)



#any()  如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true。

# >>>any(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0
# True
#
# >>> any(['a', 'b', '', 'd'])   # 列表list，存在一个为空的元素
# True
#
# >>> any([0, '', False])        # 列表list,元素全为0,'',false
# False
#
# >>> any(('a', 'b', 'c', 'd'))  # 元组tuple，元素都不为空或0
# True
#
# >>> any(('a', 'b', '', 'd'))   # 元组tuple，存在一个为空的元素
# True
#
# >>> any((0, '', False))        # 元组tuple，元素全为0,'',false
# False
#
# >>> any([]) # 空列表
# False
#
# >>> any(()) # 空元组
# False
