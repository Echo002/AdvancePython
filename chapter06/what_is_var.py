# python和Java中的变量本质不一样，python的变量实质上是一个指针 int 或 str

a = 1
# 1. a贴在1上面
# 2. 先生成对象，再贴便利贴

a = [1,2,3]
b = a
b.append(4)
print(a)
# [1, 2, 3, 4]
print(a is b)
# 判断id是否相等，True
print(id(a) == id(b))
# 判断值是否相等，调用__eq__魔法函数，True

a = [1,2,3,4]
b = [1,2,3,4]
print(a is b)
# False

a = 1
b = 1
print(a is b)
# Ture

# 在判断某个实例是不是属于某个类时 常用is
class Person:
    pass

passager = Person()
print(type(passager) is Person)
# True