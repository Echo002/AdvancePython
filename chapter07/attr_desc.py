import numbers
class IntFeild:
    # 实现下面三个任意一个魔法函数之后都会将该类变为属性描述符
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need.")
        self.value = value
    def __delete__(self, instance):
        pass

class NonDataIntField:
    # 非数据属性描述符
    def __get__(self, instance, owner):
        return self.value

class User:
    # age = IntFeild()
    age = NonDataIntField()

'''
如果user是某个类的实例，那么user.age（以及等价的getattr(user,'age')）
首先调用__getattribute__。如果定义了__getattr__方法，那么在
__getattribute__抛出AttributeError的时候会调用到__getattr__，
而对于描述符__get__的调用，则是发生在__getattribute__内部的。
user = User()，那么user.age顺序如下：
（1）如果”age“出现在User或其他基类的__dict__中，且age是data descriptor，那么调用其__get__方法
（2）如果”age“出现在obj的__dict__中，那么直接返回obj.__dict__['age']，否则
（3）如果“age”出现在User或基类的__dict__中
（3.1）如果age是non-data descriptor，那么调用其__get__方法，否则
（3.2）返回__dict__['age']
（4）如果User有__getattr__方法，调用__getattr__方法，否则
（5）抛出AttributeError
'''

if __name__ == "__main__":
    user = User()
    user.age = 30
    print(user.__dict__)
    print(user.age)