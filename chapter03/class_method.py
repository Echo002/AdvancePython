class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def valid_str(date_str):
        year, month, day = tuple(date_str.split("-"))
        if int(year) > 0 and (int(month) > 0 and int(month) <= 12) and (int(day) > 0 and int(day) <= 31):
            return True
        return False
    # 静态方法
    # 优点：
    # 问题：硬编码，修改类名称后需要同时修改函数内容
    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))

    # 类方法
    # 优点：传递进来的是类
    @classmethod
    def from_string(cls):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))

    # 类方法
    def __str__(self):
        return "{year}/{month}/{day}".format(year = self.year, month = self.month, day = self.day)

if __name__ == "__main__":
    date_str = "2018-12-31"
    # 用staticmethod完成初始化
    new_day = Date.parse_from_string(date_str)
    print(Date.valid_str(date_str))