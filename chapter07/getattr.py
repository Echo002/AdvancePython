# __getattr__：python动态特性的根本原因
# __getattr__就是在查找不到属性的时候调用
# __getattribute__优先级排在最前面调用
from datetime import date
class User:
    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info

    # 这个函数主要是可以用来做修正，比如调用的时候大小写写错等
    # 甚至加入灵活的逻辑
    def __getattr__(self, item):
        print("not find attr")
        return self.info[item]

    def __getattribute__(self, item):
        return "调用什么都是我"


if __name__ == "__main__":
    user = User("bobby", date(year=1987, month=1, day=1), info={"company":"cqupt"})
    print(user.age)
    print(user.company)