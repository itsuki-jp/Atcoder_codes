n = int(input())
d = dict()
lst = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append([a, 1])
    lst.append([a + b, -1])
lst.sort()
ans = [0 for _ in range(n + 1)]
cnt = 0
for i in range(len(lst) - 1):
    cnt += lst[i][1]
    ans[cnt] += lst[i + 1][0] - lst[i][0]
print(*ans[1:])
