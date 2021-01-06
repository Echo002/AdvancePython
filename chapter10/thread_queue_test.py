# 通过queue的方式进行线程同步
import time
import threading
import queue

def get_detal_html(queue):
    while True:
        url = queue.get()
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")

def get_detal_url(queue):
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            queue.put("http://projectsedu.com/{id}".format(id = i))
        print("get detail url end")

if __name__ == "__main__":
    detail_url_queue = queue.Queue(maxsize=1000)
    for i in range(10):
        thread = threading.Thread(target=get_detal_html, args=(detail_url_queue,))