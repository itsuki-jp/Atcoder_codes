from collections import defaultdict

n = int(input())
s = [input() for _ in range(n)]
ans = float("inf")
for i in range(10):
    i = str(i)
    d = defaultdict(int)
    for j in range(n):
        pos = s[j].index(i)
        d[pos] += 1
    mx = -1
    for j in range(11):
        if d[j] == 1:
            mx = max(mx, j)
        elif d[j] > 1:
            mx = max(mx, (d[j] - 1) * 10 + j)
    ans = min(mx, ans)
print(ans)
