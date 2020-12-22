my_list = []
my_list.append(1)
my_list.append("a")
# 容器序列可以存放不同的数据类型

from collections import abc

a = [1,2]

# 常规方式
c = a + [3, 4]
# c = a + (3, 4) 会抛出异常

# 就地加
a += [3, 4]
# a += (3, 4) 没有问题，只要是可迭代类型均可
# def __iadd__(self, values):
#     self.extend(values)
#     return self
# def extend(self, values): 无返回值
#     'S.extend(iterable) -- extend sequence by appending elements from the iterable'
#     for v in values:
#         self.append(v)
print(a)