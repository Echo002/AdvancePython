class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list
    # 魔法函数以双下划线开头和结尾，python中内置了很多魔法函数
    # 将这个类变成可迭代对象
    def __getitem__(self, item):
        return self.employee[item]
    # 开发者模式下显示 company -> repr(company)
    def __repr__(self):
        return  ",".join(self.employee)
    # 字符串显示时调用 print(company) -> print(str(company))
    def __str__(self):
        return "、".join(self.employee)

company = Company(["bob", "tom", "jane"])
print(company)

# employee = company.employee
# for em in employee:
#     print(em)
#
# # 添加完魔法函数getitem之后就可以这样写了
# for em in company:
#     print(em)