#coding=utf-8

'''写一个消费者和生产者，为了练习多线程，用多线程的方式实现，并通过类的重写的方法来实现'''
from queue import Queue
from threading import Thread
import time

#生成类，输出一堆数字
class Proceduer(Thread):
    def __init__(self,queue):
        super(Proceduer, self).__init__()
        self.queue = queue
    def run(self):
        try:
            for i in range(1,10):
                print("put data is: {0} to queue".format(i))
                self.queue.put(i)

        except Exception as e:
            print("put data error!")
            raise e

#消费者类
class Consumer_odd(Thread):
    def __init__(self,queue):
        super(Consumer_odd, self).__init__()
        self.queue = queue
    def run(self):
        try:
            while not self.queue.empty():
                number = self.queue.get()
                if number % 2 != 0:
                    print("get {0} from queue ODD".format(number))
                else:
                    self.queue.put(number)
                time.sleep(1)
        except Exception as e:
            raise e

class Consumer_even(Thread):
    def __init__(self,queue):
        super(Consumer_even, self).__init__()
        self.queue = queue
    def run(self):
        try:
            while not self.queue.empty(): #queue.empty() 
                number = self.queue.get()
                if number % 2 == 0:
                    print("get {0} from queue EVEN,thread name is: {1}".format(number, self.getName()))
                else:
                    self.queue.put(number)
                time.sleep(1)
        except Exception as e:
            raise e

def main():
    queue = Queue()

    p = Proceduer(queue=queue)
    p.start()
    p.join()
    time.sleep(1)
    c1 = Consumer_odd(queue=queue)
    c2 = Consumer_even(queue=queue)
    c1.start()
    c2.start()
    c1.join()
    c2.join()

    print("All threads terminate!")

if __name__ == '__main__':
    main()