import itertools

n = int(input())
a = list(map(int, input().split()))
lst = [a[0]] + [0] * (n - 1)
for i in range(1, n):
    lst[i] = max(lst[i - 1], a[i])
s_lst = list(itertools.accumulate(a))
s2_lst = list(itertools.accumulate(s_lst))
print(a[0] * 2)
for i in range(1, n):
    temp = s_lst[i] + lst[i] * (i + 1) + s2_lst[i - 1]
    print(temp)
