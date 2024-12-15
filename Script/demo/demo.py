import datetime
import multiprocessing
import queue
import time,threading
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing import Process
import os

# No.1 创建线程
# def get_data():
#     print("\tget_data函数开始执行，时间:{}".format(datetime.datetime.now()))
#     for i in range(1,11):
#         tips="." * i
#         print("\t正在连接{}".format("".join(tips)))
#         time.sleep(1)
#     print("\tget_data函数执行完毕，时间:{}".format(datetime.datetime.now()))
# print("主线程创建子线程")
# t = threading.Thread(target=get_data)
# print("启动子线程")
# t.start()
# print("主线程等待子线程执行完毕")
# t.join()
# print("子线程执行完毕")


# No.2 创建多个线程
# def get_data(n):
#     print("当前线程名称：{}开始执行，并休眠{}秒".format(threading.current_thread().name, n))
#     time.sleep(n)
#     print("当前线程名称：{}执行完毕".format(threading.current_thread().getName()))
# t1 = threading.Thread(target=get_data, name="A线程",args=(2,))
# t2 = threading.Thread(target=get_data, name="B线程",args=(3,))
# t1.start()
# t2.start()
# t1.join()
# print("线程{}执行完毕".format(t1.getName()))
# t2.join()
# print("线程{}执行完毕".format(t2.getName()))

# No.3 自定义线程类
# class CustomThread(threading.Thread):
#     def __init__(self,name="",num=""):
#         super().__init__()
#         self.name = name
#         self.num = num
#     def run(self):
#         print("当前线程名称：{}开始执行，并休眠{}秒".format(threading.current_thread().getName(),self.num))
#         time.sleep(self.num)
#         print("当前线程名称{}执行完毕".format(threading.current_thread().getName()))
# t1 = CustomThread("A线程",4)
# t2 = CustomThread("B线程",5)
# t1.setDaemon(True)
# t1.start()
# t2.start()
# print("T1线程活动状态：",t1.is_alive())
# print("T1线程名称：",t1.name)
# print("T1线程id：",t1.ident)
# print("T1线程是否为后台线程：{}",format(t1.isDaemon()))
# print("T2线程是否为后台线程：{}",format(t2.isDaemon()))

# No.4 线程池
# def func(num):
#     print("当前线程id：{}开始执行，休眠时间{}".format(threading.current_thread().ident,num))
#     time.sleep(num)
#     print("当前线程id：{}执行完毕".format(threading.current_thread().ident))
# def submit_task():
#     args1 = [1,2]
#     with ThreadPoolExecutor(5) as executor:
#         for i in args1:
#             executor.submit(func,i)
# def map_task():
#     args2 = [1,2,3,4,5,6]
#     with ThreadPoolExecutor(2) as executor:
#         executor.map(func,args2)
# submit_task()
# # map_task()

# No.5 线程同步
# amount = 0
# def func():
#     global amount
#     thread_lock.acquire()
#     for i in range(1000000):
#         amount += 1
#         amount -= 1
#     thread_lock.release()
#     print("线程：{}得到结果：{}".format(threading.current_thread().ident, amount))
# thread_lock = threading.Lock()
# t1 = threading.Thread(target=func)
# t2 = threading.Thread(target=func)
# t1.start()
# t2.start()

#No.6 死锁
# amount = 0
# def func1():
#     global amount
#     t1_thread_lock.acquire()
#     print("t1线程获得t1_thread_lock 锁")
#     time.sleep(1)
#     print("t1线程尝试获得t2_thread_lock 锁")
#     t2_thread_lock.acquire()
#     print("t1线程获得t2_thread_lock 锁")
#     for i in range(1000000):
#         amount += 1
#         amount -= 1
#     t2_thread_lock.acquire()
#     t1_thread_lock.release()
#     print("线程：{}得到的结果：{}".format(threading.current_thread().ident, amount))
# def func2():
#     global amount
#     t2_thread_lock.acquire()
#     print("t2线程获得t2_thread_lock 锁")
#     time.sleep(1)
#     print("t2线程尝试获得t1_thread_lock 锁")
#     t1_thread_lock.acquire()
#     print("t1线程获得t2_thread_lock 锁")
#     for i in range(1000000):
#         amount += 1
#         amount -= 1
#     t1_thread_lock.acquire()
#     t2_thread_lock.release()
#     print("线程：{}得到的结果：{}".format(threading.current_thread().ident, amount))
# t1_thread_lock = threading.Lock()
# t2_thread_lock = threading.Lock()
# t1 = threading.Thread(target=func1)
# t2 = threading.Thread(target=func2)
# t1.start()
# t2.start()
# 输出结果；
# t1线程获得t1_thread_lock 锁
# t2线程获得t2_thread_lock 锁
# t2线程尝试获得t1_thread_lock 锁
# t1线程尝试获得t2_thread_lock 锁

# No.9线程同步
# amount = 0
# def func1():
#     global amount
#     thread_id = threading.current_thread().ident
#     cond.acquire()
#     print("线程{}获得锁".format(thread_id))
#     print("线程{}发出通知".format(thread_id))
#     cond.notify()
#     print("线程{}线程挂起，等待通知".format(thread_id))
#     cond.wait()
#     for i in range(1000000):
#         amount += 1
#         amount -= 1
#     print("线程{}执行业务代码后发出通知".format(thread_id))
#     cond.notify()
#     print("线程{}释放锁".format(thread_id))
#     cond.release()
#     print("线程{}得到的结果:{}".format(thread_id, amount))
# def func2():
#     global amount
#     thread_id = threading.current_thread().ident
#     time.sleep(3)
#     cond.acquire()
#     print("\t\t\t线程{}获得锁".format(thread_id))
#     for i in range(1000000):
#         amount += 1
#         amount -= 1
#     print("\t\t\t线程{}业务代码执行完毕发出通知".format(thread_id))
#     cond.notify()
#     print("\t\t\t线程{}挂起，等待通知".format(thread_id))
#     cond.wait()
#     print("\t\t\t线程{}释放锁".format(thread_id))
#     cond.release()
#     print("\t\t\t线程{}得到的结果：{}".format(thread_id, amount))
# cond = threading.Condition()
# t1 = threading.Thread(target=func1)
# t2 = threading.Thread(target=func2)
# t1.start()
# t2.start()

# No.10 进程
# def proc():
#     print("子进程id:{}".format(os.getpid()))
# if __name__ == '__main__':
#     print("当前进程：{} 创建子进程".format(os.getpid()))
#     p = Process(target=proc)
#     print("启动子进程")
#     p.start()
#     print("等待子进程结束")
#     p.join()
#     print("主、子进程结束")

# No.11 进程池
# def func(num):
#     print("当前进程id：{}开始执行，休眠时间{}".format(os.getpid(),num))
#     time.sleep(num)
#     print("当前进程id：{}执行完毕".format(os.getpid()))
# if __name__ == '__main__':
#     args1 = [1,2,3,4,5,6]
#     # with ProcessPoolExecutor(5) as executor:
#     #     for i in args1:
#     #         executor.submit(func, i)
#     with ProcessPoolExecutor(5) as executor:
#         executor.map(func, args1)

from multiprocessing import Queue,Process

# No.12 生产者和消费者
# def set_msg(que):
#     print("生产者进程id：{}".format(os.getpid()))
#     for i in range(3):
#         print("数据{}入队".format(i))
#         que.put(i)
#         time.sleep(i)
# def get_msg(que):
#     time.sleep(1)
#     print("\t消费者者进程id：{}".format(os.getpid()))
#     while not que.empty():
#         data = que.get(True)
#         print("从队列获取数据：{}".format(data))
#         time.sleep(1)
# if __name__ == '__main__':
#     q = Queue()
#     producer = Process(target=set_msg, args=(q,))
#     consumer = Process(target=get_msg, args=(q,))
#     producer.start()
#     consumer.start()

# No.12 进程锁
# amount = 0
# def func(lock):
#     global amount
#     lock.acquire()
#     for i in range(1000000):
#         amount += 1
#         amount -= 1
#     lock.release()
#     print("进程id:{}得到的结果：{}".format(os.getpid(),amount))
#
# if __name__ == '__main__':
#     process_lock = multiprocessing.Lock()
#     p1 = multiprocessing.Process(target=func, args=(process_lock,))
#     p2 = multiprocessing.Process(target=func, args=(process_lock,))
#     p1.start()
#     p2.start()

# No.13 协程
# def consumer():
#     print("consumer开始运行：")
#     count = 0
#     while True:
#         print("A:consumer使用yield返回消息给producer")
#         num = yield + count
#         count += 100
#         print("D:consumer收到消息：{}".format(num))
#
# def producer(gen):
#     num = gen.send(None)
#     print("B:producer首次收到消息为{}".format(num))
#     for i in range(1,3):
#         print("C:producer发送消息：{}到consumer".format(i))
#         num = gen.send(i)
#         print("E:producer收到消息：{}".format(num))
# generator = consumer()
# producer(generator)

# No.14 greenlet创建协程
# from greenlet import greenlet
# def consumer():
#     while True:
#         print("执行Consumer")
#         time.sleep(1)
#         producer_greenlet.switch()
# def producer():
#     while True:
#         print("执行Producer")
#         time.sleep(1)
#         consumer_greenlet.switch()
# producer_greenlet = greenlet(producer)
# consumer_greenlet = greenlet(consumer)
# producer_greenlet.switch()
# 执行Producer
# 执行Consumer
# 执行Producer
# 执行Consumer
# 执行Producer
# 执行Consumer
# 执行Producer

# No.15 使用gevent创建协程
import gevent
def consumer(m):
    n = 0
    while n<m:
        print("consumer协程名称：{} n:{}".format(gevent.getcurrent().name,n))
