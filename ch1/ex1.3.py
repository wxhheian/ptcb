from collections import deque

def search(lines,pattern,history=5):
    previous_lines = deque(maxlen=history)                   #创建一个空的deque队列   deque([], maxlen=5)  previous_lines只有5行
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)

#examle use on a file
if __name__ == '__main__':
    with open(r'somefile.txt') as f:                               #f为文件object
        for line,prevlines in search(f,'Python',5):
            for pline in prevlines:
                print(pline,end='')
            print(line,end='')
            print('-'*20)





# f=open(r'somefile.txt')
# g=search(f,'Python',5)
# print(next(g))
# print(next(g))
# print(next(g))
