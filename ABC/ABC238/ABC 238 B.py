n = int(input())
a = list(map(int, input().split()))
lst = [0, 360]
now = 0
for _ in a:
    now += _
    now %= 360
    lst.append(now)
ans = 0
lst.sort()
for i in range(len(lst) - 1):
    ans = max(ans, lst[i + 1] - lst[i])
print(ans)
