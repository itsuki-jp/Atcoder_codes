import itertools
n, k = map(int,input().split())
list1 = []
for i in range(k):
    d = int(input())
    a = list(map(int,input().split()))
    list1.append(a)
b = list(itertools.chain.from_iterable(list1))
b = set(b)

print(n - len(b))