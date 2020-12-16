from chapter03.class_method import Date
class User:
    def __init__(self, birthday):
        # 变量前加__表示私有属性，无法直接访问
        self.__birthday = birthday

    def get_age(self):
        return 2018 - self.__birthday.year

if __name__ == "__main__":
    user = User(Date(1990,2,1))
    print(user.get_age())
    # 还是可以访问私有属性的，没有在语言层面实现私有
    print(user._User__birthday)
    # print(user.__birthday)