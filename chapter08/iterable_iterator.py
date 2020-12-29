from collections.abc import Iterator
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list
    # 魔法函数以双下划线开头和结尾，python中内置了很多魔法函数
    # 将这个类变成可迭代对象
    # def __getitem__(self, item):
    #     return self.employee[item]
    # 开发者模式下显示 company -> repr(company)

    def __iter__(self):
        return MyIterator(self.employee)
    def __repr__(self):
        return  ",".join(self.employee)
    # 字符串显示时调用 print(company) -> print(str(company))
    def __str__(self):
        return "、".join(self.employee)

class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0
    # 迭代器中可以直接返回自己，如果继承了Iterator
    # 可以不用重写__iter__
    # def __iter__(self):
    #     return self

    # 真正返回迭代值的逻辑，不支持切片
    def __next__(self):
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


if __name__ == "__main__":
    company = Company(["bob", "tom", "jane"])
    my_itor = iter(company)
    while True:
        try:
            print(next(my_itor))
        except StopIteration:
           pass

    # for item in company:
    #     print(item)