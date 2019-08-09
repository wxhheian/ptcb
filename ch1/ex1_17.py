#从字典中提取子集
def sub_dict():
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
}
    #make a dictionary of all prices over 200
    #使用字典推导
    p1 = {key:value for key,value in prices.items() if value > 200}
    #make a dictionary of tech stocks
    tech_name = {'AAPL','IBM','HPQ','MSFT'}
    p2 = {key:value for key,value in prices.items() if key in tech_name}
    print(p1)
    print(p2)

    #创建一个元组序列，然后将它传递给dict()
    p11 = dict((key,value) for key,value in prices.items() if value > 200)
    p22 = { key:prices[key] for key in prices.keys() & tech_name}
    print(p11)
    print(p22)

if __name__ == '__main__':
    sub_dict()
