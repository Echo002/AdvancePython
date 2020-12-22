# 类也是对象，type是创建类的类
# 通过函数动态创建类
def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user！"
        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company

# 问题：虽然能动态创建类，但是还是不是很灵活
# 元类
class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

class User(metaclass=MetaClass):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "user"

# python中类实例化的过程，会首先寻找metaclass，通过metaclass去创建user类
# type去创建类对象

def say(self):
    return "i am an user."

class BaseClass(metaclass=MetaClass):
    def answer(self):
        return "i am a baseclass."

if __name__ == "__main__":
    # Myclass = create_class("user")
    # my_obj = Myclass()
    # print(my_obj)

    # type动态创建类
    # User = type("User", (BaseClass, ), {"name":"xugao", "say":say})

    # 元类创建类
    myObj = User(name="xugao")
    print(myObj.name)
    # print(myObj.say())
    print(myObj)