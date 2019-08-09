from collections import deque


def search(lines, pattern, history=5):
    result = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            result.append(line)
    yield result


with open('test.txt', 'r') as f:
    for pattern_result in search(f, 'python', history=5):
        for one_line in pattern_result:
            print(one_line,end='')
