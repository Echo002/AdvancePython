class A:
    pass

class B(A):
    pass

b = B()

print(isinstance(b, B))
print(isinstance(b, A))
print(type(b) is B)
print(type(b) is A)
# type()不会认为子类是一种父类类型，不考虑继承关系
# isinstance()会认为子类是一种父类类型，考虑继承关系
# is 判断id是否相同
# == 判断值是否相等