##排序相同类型相同的对象，但不支持原生的比较操作
##你在应用程序里有一个User实例序列，，并且希望通过user_id属性进行排序

class User:
    def __init__(self,user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)

def sort_notcompare():
    users = [User(23),User(3),User(99)]
    print(users)
    print(sorted(users,key=lambda u:u.user_id))


if __name__ == '__main__':
    sort_notcompare()
