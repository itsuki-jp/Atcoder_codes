def get_sieve_of_eratosthenes( n ):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = [2]
    limit = int(n ** 0.5)
    data = [(i + 1) for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


q = int(input())
lst = [0] * (10 ** 5 + 1)
prime_lst = set(get_sieve_of_eratosthenes(10 ** 5))
for i in range(10 ** 5):
    if i in prime_lst and (i + 1) / 2 in prime_lst:
        lst[i + 1] = 1
    lst[i + 1] += lst[i]
for _ in range(q):
    l, r = map(int, input().split())
    print(lst[r + 1] - lst[l])
