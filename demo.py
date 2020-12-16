class Foo:
    @classmethod
    def Print(cls):
        print("Foo的类方法调用")

class Son(Foo):
    @classmethod
    def Print(cls):
        print("Son的类方法调用")

son = Son()
son.Print()