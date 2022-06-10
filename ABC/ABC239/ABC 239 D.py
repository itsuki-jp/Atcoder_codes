# -*- coding:utf-8 -*-
import math


def get_sieve_of_eratosthenes( n ):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


a, b, c, d = map(int, input().split())
lst = set(get_sieve_of_eratosthenes(300))
for x in range(a, b + 1):
    for y in range(c, d + 1):
        total = x + y
        if total  in lst:
            break
    else:
        exit(print("Takahashi"))
print("Aoki")
