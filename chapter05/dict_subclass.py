# 不建议继承list和dict
# class Mydict(dict):
#     def __setitem__(self, key, value):
#         super().__setitem__(key, value * 2)

from collections import defaultdict
my_dict = defaultdict(dict)
my_value = my_dict['bobby']
print(my_dict)
# defaultdict(<class 'dict'>, {'bobby': {}})
