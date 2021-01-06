from concurrent.futures import ThreadPoolExecutor, as_completed
import time
# 线程池：
# 主线程中获取某一个线程或任务的状态，并获取返回值
# 当一个线程完成的时候主线程能立即知道
# futures可以让多线程和多进程编码一致

def get_html(times):
    time.sleep(times)
    print("got page {} susess!".format(times))
    return times

executor = ThreadPoolExecutor(max_workers=2)
# 通过submit函数提交执行的函数到线程池中,submit立即返回
# task1 = executor.submit(get_html, (3))
# task2 = executor.submit(get_html, (2))
# task3 = executor.submit(get_html, (1))

# done：判断某个任务是否完成
# cancel：取消任务
# print(task1.done())
# print(task2.cancel()) # 只能在没有开始的时候取消，进行中和已完成都会返回false
# time.sleep(3)
# print(task1.done())

# result：获取执行结果
# print(task1.result())


urls = [4, 3, 2]
# 获取已经成功的task状态
# all_task = [executor.submit(get_html, (url)) for url in urls]
# for future in as_completed(all_task):
#     data = future.result()
#     print("get {} page success".format(data))

# 通过executor的map获取已经完成的task的值
for data in executor.map(get_html, urls):
    print("get {} page success".format(data))
