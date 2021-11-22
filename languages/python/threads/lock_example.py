#!/usr/bin/env python3

import threading
import logging
import time
import random


'''
Example formatter line 
%(asctime)s %(levelname)s %(threadName)s %(name)s   %(filename)s:%(funcName)s   %(message)s"
'''

logging.basicConfig(level=logging.DEBUG, format='%(threadName)-9s %(funcName)s() %(message)s',)

class Counter(object):
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug("Waiting for lock")
        self.lock.acquire()
        try:
            logging.debug("Lock aquired")
            self.value += 1
        finally:
            self.lock.release()
            logging.debug("Release lock")

    def incrementSecondLockingMethod(self):
        'This method also can be used to acqurie a lock'
        logging.debug("Waiting for lock")
        with self.lock:
            logging.debug("Lock aquired")
            try:
                self.value += 1
            finally:
                logging.debug("Release lock")


def worker(c):
    for i in range(2):
        r = random.random()
        logging.debug("sleep %0.02f seconds"% r)
        time.sleep(r)
        c.increment()
    logging.debug("Done")


if __name__ == "__main__":
    counter_obj = Counter()
    thread_list = []

    for i in range(2):
        t = threading.Thread(target=worker, args=(counter_obj, ))
        t.start()
        thread_list.append(t)

    logging.debug("waiting for worker threads")

    for t in thread_list:
        t.join()

    logging.debug("End of program.. Counter calue %d", counter_obj.value)







