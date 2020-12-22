# set 集合 frozenset（不可变集合）无序集合，不重复
# frozen一般作为dict的key
s = set(['a', 'b', 'c', 'd', 'e'])

s1 = {'a', 'b'}
# print(type(s1))

s2 = frozenset("abcde")
# print(s2)

other_set = set("ce")

# 向set添加数据
s.update(other_set)
# print(s)
# {'e', 'b', 'c', 'd', 'y', 'z', 'x', 'a'}

# 比较两个set 留下的是s剩余的元素
# 注意这些 | & -集合运算
re_set = s.difference(other_set)
# print(re_set)
# {'b', 'a', 'd'}
