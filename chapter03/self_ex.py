from chapter03.class_method import Date
class Person:
    '''人'''
    name = "user"

class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name

if __name__ == "__main__":
    user = Student("Bob")
    # 通过__dict__查询属性
    print(user.__dict__)
    user.__dict__["school_addr"] = "北京市"
    print(Person.__dict__)
    print(user.school_addr)
    print(dir(user))