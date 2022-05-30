import math
import time


def func1( n ):
    start = time.time()
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return time.time() - start
        prime.append(p)
        data = [e for e in data if e % p != 0]


def func2( n ):
    start = time.time()
    res = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            res.append(i)
    return time.time() - start


SIZE = 10**5
print(func1(SIZE))  # 0.11秒
print(func2(SIZE))  # 49秒
