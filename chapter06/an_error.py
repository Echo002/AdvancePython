def add(a, b):
    a += b
    return a

class Company:
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs
    def add(self, staff_name):
        self.staffs.append(staff_name)
    def remove(self, staff_name):
        self.staffs.remove(staff_name)

if __name__ == "__main__":
    a = 1
    b = 2
    c = add(a, b)
    print("{},{}".format(a,b))
    print(c)
    '''
    1,2
    3
    '''

    a = [1, 2]
    b = [3, 4]
    c = add(a, b)
    print("{},{}".format(a, b))
    print(c)
    '''
    [1, 2, 3, 4],[3, 4]
    [1, 2, 3, 4]
    '''

    a = (1, 2)
    b = (3, 4)
    c = add(a, b)
    print("{},{}".format(a, b))
    print(c)
    '''
    (1, 2),(3, 4)
    (1, 2, 3, 4)
    '''

    com1 = Company("com1", ["bobby1", "bobby2", "bobby3"])
    com1.add("bobby4")
    com1.remove("bobby1")
    print(com1.staffs)
    # ['bobby2', 'bobby3', 'bobby4']

    com2 = Company("com2")
    com2.add("bobby")
    print(com2.staffs)
    # ['bobby']

    com3 = Company("com3")
    com3.add("bobby5")
    print(com2.staffs)
    print(com3.staffs)
    # ['bobby', 'bobby5']
    # ['bobby', 'bobby5']
    print(com2.staffs is com3.staffs)

    # com2和com3使用了默认的list，list属于可变对象，此时com2和com3共用一个list
    print(Company.__init__.__defaults__)
    # (['bobby', 'bobby5'],)
    # 结论：尽量不要将list作为函数参数传入