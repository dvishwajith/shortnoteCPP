#!/usr/bin/env python3

import multiprocessing
import time
import random
from functools import reduce


def func(number):
    random_list = random.sample(range(1000000), number)  #  """Chooses k unique random elements from a population sequence or set.
    return reduce(lambda x, y: x*y, random_list)


number = 50000

process1 = multiprocessing.Process(target=func, args=(number,))
process2 = multiprocessing.Process(target=func, args=(number,))

process1.start()
process2.start()

process1.join()
process2.join()
