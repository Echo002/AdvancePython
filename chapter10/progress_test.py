# 多进程编程
# 1. 耗CPU的操作使用多线程无法发挥多核优势
# 2. 对于IO操作来说，使用多线程编程，进程切换代价高于线程

# 对于耗费CPU的操作，多进程优于多线程
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

# print(fib(3))

# 对于耗费IO的操作，多线程优于多进程
def random_sleep(n):
    time.sleep(n)
    return n

if __name__ == "__main__":
    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2]*30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result : {}".format(data))
            # print("get {} page success".format(data))
        print("last time is {}".format(time.time()-start_time))