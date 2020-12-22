class User:
    # new传入的是类，可以自定义生成过程
    def __new__(cls, *args, **kwargs):
        print("in new")
        return super().__new__(cls)

    # init是用来完善对象的
    def __init__(self, name):
        print("in init")
        self.name = name

if __name__ == "__main__":
    # 如果new方法不返回对象，则不会调用init函数
    user = User(name="bobby")
