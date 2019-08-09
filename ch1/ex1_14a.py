#返回从其操作数获取属性的可调用对象。如果请求多个属性，则返回属性元组
class User:
    def __init__(self,user_id,last_name,first_name):
        self.user_id = user_id
        self.last_name = last_name
        self.first_name = first_name
    def __repr__(self):
        #return 'User({})'.format(self.user_id)
        return 'User({}){}{}'.format(self.user_id,self.first_name,self.last_name)

from operator import attrgetter
def sort_notcompare():
    users = [User(23,'wang','xinhao'),User(3,'ma','yun'),User(99,'ma','huateng')]
    print(users)
    #print(sorted(users,key=attrgetter('user_id')))
    print(sorted(users,key=attrgetter('last_name','first_name')))


if __name__ == '__main__':
    sort_notcompare()


#min(users,key=attrgetter('user_id'))
#max(users,key=attrgetter('user_id'))
