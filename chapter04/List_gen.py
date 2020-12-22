# 列表推导式
# 提取1-20之间的奇数
odd_list = [i for i in range(20) if i % 2 != 0]
# 添加复杂的功能
def handle_tiem(item):
    return item * item
odd_list = [handle_tiem(i) for i in range(20) if i % 2 != 0]

# 列表生成式的性能高于列表操作
print(odd_list)

# 生成器表达式
# 这不是set，会变成一个生成器
odd_gen = (i for i in range(20) if i % 2 != 0)
print(type(odd_list))

# 字典推导式
my_dict = {"bobb0":22, "bobb1":23, "bobby2":24}
reversed_dict = {value:key for key, value in my_dict.items()}
print(reversed_dict)

# 集合推导式
my_set = {key for key, value in my_dict.items()}
print(type(my_set))
print(my_set)