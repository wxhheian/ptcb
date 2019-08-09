import pandas as pd
import numpy as np

df = pd.DataFrame({'key1':list('aabba'),
                   'key2':['one','two','one','two','one'],
                   'data1':np.random.randn(5),
                   'data2':np.random.randn(5)})
print(df)
for i in df.groupby('key1'):              #一个维度
    print(i)

for i in df.groupby(['key1','key2']):
    print(i)


#输出结果
      data1     data2 key1 key2
0  0.269072 -0.762194    a  one
1  0.368193  1.287270    a  two
2  1.402914 -0.222861    b  one
3 -0.013069  0.227899    b  two
4  0.343544  0.835015    a  one
('a',       data1     data2 key1 key2
0  0.269072 -0.762194    a  one
1  0.368193  1.287270    a  two
4  0.343544  0.835015    a  one)
('b',       data1     data2 key1 key2
2  1.402914 -0.222861    b  one
3 -0.013069  0.227899    b  two)
(('a', 'one'),       data1     data2 key1 key2
0  0.269072 -0.762194    a  one
4  0.343544  0.835015    a  one)
(('a', 'two'),       data1    data2 key1 key2
1  0.368193  1.28727    a  two)
(('b', 'one'),       data1     data2 key1 key2
2  1.402914 -0.222861    b  one)
(('b', 'two'),       data1     data2 key1 key2





3 -0.013069  0.227899    b  two)
