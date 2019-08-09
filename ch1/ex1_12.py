#怎么样找出一个序列中出现次数最多的元素？
from collections import Counter
def most_frequency():
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
]
    word_counts = Counter(words)
    top_three = word_counts.most_common(3)
    print(top_three)

if __name__ == '__main__':
    most_frequency()
