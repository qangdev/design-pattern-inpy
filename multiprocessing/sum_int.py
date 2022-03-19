
import random
import multiprocessing


def compute(n):
    return sum([
        random.randint(1,100) for _ in range(10000000)
    ])

pool = multiprocessing.Pool(processes=8)
print("Result: %s" % (pool.map(compute, range(8))))
