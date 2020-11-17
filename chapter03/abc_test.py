from collections.abc import Sized
# 检查某个类是否有某种方法
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list
    def __len__(self):
        return len(self.employee)

com = Company(['1', '2', '3'])
print(len(com))

# 判断com类中，是否有__len__函数
print(hasattr(com, "__len__"))

# 1. 判断com类是否是某个数据类型
print(isinstance(com, Sized))

# 2. 强制某个子类必须实现某些方法
# 这种方法有一个问题，只有在调用的时候才会抛出异常，
# 有时候我们希望初始化的时候就开始检查
# class CacheBase():
#     def get(self, key):
#         # 不重写就抛异常
#         raise NotImplementedError
#     def set(self, key, value):
#         raise NotImplementedError
#
# class RedisCache(CacheBase):
#     def set(self, key, value):
#         pass
#
# redis_cache = RedisCache()
# redis_cache.set('key', 'value')

# 模拟抽象类
import abc
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass
    @abc.abstractmethod
    def set(self, key, value):
        pass

class RedisCache(CacheBase):
    pass
redis_cache = RedisCache()