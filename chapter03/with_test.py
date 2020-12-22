# try except finally
def exe_try():
    try:
        f_read = open("boddy.txt")
        print("code started")
        raise KeyError
        return 1
        # raise KeyError
    # 抛出该异常时调用
    except KeyError as e:
        print("Key error")
        return 2
    # 除此之外的异常抛出调用
    else:
        print("other error")
        return 3
    # 无论是否抛出异常都会调用
    # 常用于文件关闭
    finally:
        # f_read.close()
        print("finally")
        return 4

# 上下文管理器（协议）
class Sample():
    def __enter__(self):
        print("enter")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
    def do_something(self):
        print("do something")

with Sample() as sample:
    # 这里上下文管理相当于自动调用了__enter__和__exit__
    sample.do_something()

# if __name__ == "__main__":
#     result = exe_try()
#     print(result)