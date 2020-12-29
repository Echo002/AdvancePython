# 什么是迭代协议
# 迭代器是什么？访问集合内元素的一种方式，一般用来遍历数据
# 迭代器和以下访问方式不一样，迭代器是不能返回的，提供了一种惰性方式访问数据
# [] list 是因为实现了__iter__
# 迭代器必须实现 __next__

from collections.abc import Iterable, Iterator
a = [1, 2]
iter_rator = iter(a)
print(isinstance(a, Iterable))
# True
print(isinstance(iter_rator, Iterator))
# True