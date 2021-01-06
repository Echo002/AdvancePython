import threading
from threading import Lock
from threading import Condition
# from threading import Condition
# 条件变量，用于复杂的线程同步

class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print("{} : 在".format(self.name))
            self.cond.notify()



class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫精灵")
        self.cond = cond

    def run(self):
        # 使用with语句代替self.cond.acquire...self.cond.release
        with self.cond:
            print("{} : 小爱同学".format(self.name))
            self.cond.notify()
            self.cond.wait()

if __name__ == "__main__":
    cond = threading.Condition()
    tianmao = TianMao(cond)
    xiaoai = XiaoAi(cond)

    # 天猫先说，但是小爱必须先启动，先监听
    # 在调用cond之后才能调用wait和notify方法
    xiaoai.start()
    tianmao.start()

