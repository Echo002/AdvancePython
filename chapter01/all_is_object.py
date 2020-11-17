def ask(name = "bobby"):
    print(name)

class Person:
    def __init__(self):
        print("bobby")

obj_list = []
obj_list.append(ask)
obj_list.append(Person)
# for item in obj_list:
#     print(item())

# 装饰器
def decorator_func(item):
    print("start")
    return ask

my_ask = decorator_func(ask)
my_ask("Tom")
# my_func = ask
# my_func("bobby")

# myclass = Person
# myclass()