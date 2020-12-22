import numbers
class Group:
    # 支持切片操作
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        return self.staffs.reverse()

    def __getitem__(self, item):
        # return self.staffs[item]
        # 这里有一个问题：return的值成了列表，需求应该是还返回Group类
        # 修改方式如下：
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])
    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False
staffs = ["bobby1", "bobby2", "bobby3"]
group = Group(company_name="imoc", group_name="user", staffs=staffs)
print(len(group))
if "bobby1" in group:
    print("YES")
reversed(group)
pass