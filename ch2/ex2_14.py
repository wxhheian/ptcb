#你想将几个小的字符串合并为一个大的字符串

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

def combine(source,maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)                 #注意这里是len(part) 不是 += 1  目的是控制总字符数量
        if size > maxsize:                 ##如果maxsize很大，实际上这段if代码没有作用；思考maxsize=2结果会怎么样
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)




def join_str():
    ####待合并的字符串在一个序列或者iterable里，使用join（）方法
    parts = ['Is','Chicago','Not','Chicago?']
    print(' '.join(parts))
    print(','.join(parts))
    print(''.join(parts))

    #少数的字符串用 +
    a = 'Is Chicago'
    b = 'Not Chicago?'
    c = 'ccc'
    print(a + ' ' + b)
    print('{} {}'.format(a,b))

    # a = 'Hello' 'World'
    # print(a)   #Output:HelloWorld

    ##转换数据为字符串的同时合并字符串
    data = ['ACME',50,91.1]
    print(','.join(str(d) for d in data))

    ##代码美观问题
    print(a + ':' + b + ':' + c)  # Ugly
    print(':'.join([a, b, c]))  # Still ugly
    print(a, b, c, sep=':')  # Better

    #编写构建大量小字符串的输出代码，使用生成器
    text = ''.join(sample())
    print(text)
    # for part in sample():
    #     f.write(part)



    # 混合方案
    # with open('filename','w') as f:
    #     for part in combine(sample(),32768):
    #         f.write(part)
    for part in combine(sample(), 32768):
        print(part)






if __name__ == '__main__':
    join_str()
