import time
import threading
def get_detal_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")

def get_detal_url(url):
    print("get detail url started")
    time.sleep(2)
    print("get detail url end")

# 2. 通过继承Thread类来实现多线程编程
class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name = name)
    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")

class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)
    def run(self):
        print("get detail url started")
        time.sleep(2)
        print("get detail url end")

if __name__ == "__main__":
    # 第一种方法：
    # thread1 = threading.Thread(target=get_detal_html, args=("",))
    # thread2 = threading.Thread(target=get_detal_url, args=("",))
    # 1. 设置为守护线程，当主线程退出时将它们也退出
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)
    #
    # thread1.start()
    # thread2.start()
    #
    # # 2. 等待该线程完成后，才能继续用下运行。
    # thread1.join()
    # thread2.join()

    # 第二种方法
    thread1 = GetDetailHtml("getHtml")
    thread2 = GetDetailUrl("getUrl")

    # 主线程退出时，子线程kill
    start_time = time.time()
    print("time: {}".format(time.time() - start_time))

