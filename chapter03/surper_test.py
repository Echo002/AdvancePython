from threading import Thread
class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D")
        super(D, self).__init__()



# 既然我们重写了B的构造函数，为什么还要去调用super？
'''
class Mythread(Thread):
    def __init__(self, name, user):
        self.user = user
        super().__init__(name=name)
'''
# super到底执行的顺序是什么样的？
'''
调用MRO优先级算法的下一个类
'''

if __name__ == "__main__":
    print(D.__mro__)
    d = D()