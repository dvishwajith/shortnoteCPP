#!/usr/bin/env python3

import _thread
import time


def print_time(thread_name, delay, cycles):
    count = 0
    while count < cycles: 
        time.sleep(delay)
        count += 1
        print("%s :%s counter %d" % (thread_name, time.ctime(time.time()), count))


_thread.start_new_thread(print_time, ("thread_1", 1, 10))
_thread.start_new_thread(print_time, ("thread_2", 1, 10))

while 1:
    pass