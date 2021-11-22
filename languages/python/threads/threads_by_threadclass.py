#!/usr/bin/env python3

import threading
import time
import random
from functools import reduce


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("startin thread ", self.name)
        print_time(self.name, self.counter, 1)
        print("Ending thread ", self.name)


def print_time(threadName, counter, delay):
    while counter:
        time.sleep(delay)
        print("%s : %s" % (threadName, time.ctime(time.time())))
        counter -= 1
    

# create new threads
thread1 = MyThread(1, "Thraed-1", 10)
thread2 = MyThread(1, "Thraed-2", 8)

# start new thread
thread1.start()
thread2.start()

thread1.join()
thread2.join()
