import collections
n = int(input())
a = list(map(int,input().split()))

list_1 = collections.Counter(a)

for i in range(n):
    print(list_1[(i+1)])