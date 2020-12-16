class A:
    # 类变量
    aa = 1
    def __init__(self, x, y):
        # 实例变量
        self.x = x
        self.y = y

a = A(2,3)
print(a.aa, a.x, a.y)
# 类和实例获取变量时都是向上查找
print(A.aa) # 可以找到
# print(A.x) # 不可以找到