# python中垃圾回收的算法是采用 引用计数
a = 1
b = a
# python中的del是将引用计数-1
# 回收时调用的是__del__魔法函数
del a
print("b = {}".format(b))
print("a = {}".format(a))