prices = {
    'ACME':45.23,
    'AAPL':612.78,
    'IBM':205.55,
    'HPQ':37.20,
    'FB':10.75
}

min_price = min(zip(prices.values(),prices.keys()))              ##zip()函数创建的是一个只能访问一次的迭代器
max_price = max(zip(prices.values(),prices.keys()))                   ##将（键，值）反转  #同时返回键和值

#min_price is (10.75,'FB')
#max_price is (612.78,'APPL')

#prices_and_names = zip(prices.values(),prices.keys())
# print(min(prices_and_names))   # is OK
# print(max(prices_and_names))    #max() arg is an empty sequence

min(prices)    #Return 'AAPL'
max(prices)    #Return 'IBM'

>>> min(prices.values())
10.75
>>> max(prices.values())
612.78
>>>

>>> min(prices,key=lambda k:prices[k])
'FB'
>>> max(prices,key=lambda k:prices[k])
'AAPL'

>>> prices = {'AAA':45.26,'BBB':45.26}                    ##当值一样时，键的大小决定返回结果
>>> prices
{'AAA': 45.26, 'BBB': 45.26}
>>> min(zip(prices.values(),prices.keys()))
(45.26, 'AAA')
>>> max(zip(prices.values(),prices.keys()))
(45.26, 'BBB')
>>>
