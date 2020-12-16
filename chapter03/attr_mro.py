# class A:
#     name = "A"
#     def __init__(self):
#         self.name = "obj"
#
# # 先查询实例，在向上查询（类）
# a = A()
# print(a.name)
#
# # MRO算法
# # Python2中是深度优先，python3中是广度优先

class D:
    pass

class C(D):
    pass

class B(D):
    pass

class A(B, C):
    pass

print(A.__mro__)