# -*- coding: UTF-8 -*- 
# Creator：LeK
# Date：2022/10/9

import threading
import time
from queue import Queue


def thread_job():
    print('T1 start\n')
    print("This is an added Thread, number is %s\n" % threading.current_thread())
    for i in range(3):
        time.sleep(1)
    print('T1 finish')


def thread2_job(list, q):
    for i in range(len(list)):
        list[i] = list[i] ** 2
    q.put(list)


def thread3_job():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 1
        print('job1', A)
    lock.release()


def thread4_job():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 10
        print('job2', A)
    lock.release()


def main():
    added_thread = threading.Thread(target=thread_job, name='T1')  # 添加线程
    added_thread.start()  # 运行线程
    added_thread.join()  # 阻塞主线程
    print('This is main function.')

    print(threading.active_count())  # 返回正在运行线程的数量，相当于len(threading.enumerate())
    print(threading.enumerate())  # 返回一个正在运行线程的列表
    print(threading.current_thread())  # 返回当前线程变量

    # 使用Queue队列返回多线程的结果
    q = Queue()
    data = [[1, 2, 3], [3, 4, 5], [4, 4, 4], [5, 5, 5]]
    threads = []
    for i in range(4):
        t = threading.Thread(target=thread2_job, args=(data[i], q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    result = []
    for _ in range(4):
        result.append(q.get())
    print(result)

    # 锁
    global A,lock
    A = 0
    lock = threading.Lock()
    t1 = threading.Thread(target=thread3_job)
    t2 = threading.Thread(target=thread4_job)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()
