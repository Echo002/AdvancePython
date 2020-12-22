from collections.abc import Mapping
# dict属于Mapping类型
a = {}
print(isinstance(a, Mapping))

a = {"bobby1":{"company":"imooc"},
     "bobby2":{"company":"imooc"},
     "bobby3":{"company":"imooc"}}

# 清除字典
# a.clear()
# copy,返回浅拷贝
# new_dict = a.copy()
# new_dict["bobby1"]["company"] = "imooc3"
import copy
new_dict = copy.deepcopy(a)
new_dict["bobby1"]["company"] = "imooc3"

# formkeys
# Python 字典 fromkeys() 函数用于创建一个新字典，
# 以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
new_list = ["bobby1", "bobby2", "bobby3"]
new_dict = dict.fromkeys(new_list, {"company":"imooc"})
pass

# get 不会抛出异常，自定义没有的键值
# print(new_dict["bobby"]) 当键值不存在会抛出异常
print(new_dict.get("bobby", {}))

# items
for key, value in new_dict.items():
    print("{}, {}".format(key, value))

# setdefault
# 和 get()方法 类似, 如果键不存在于字典中，将会添加键并将值设为默认值。
print(new_dict["bobby1"])
print(new_dict.setdefault("bobby1", "google"))
# {'company': 'imooc'}
print(new_dict.setdefault("bobbyx", "google"))
# google
