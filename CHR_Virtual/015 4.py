n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
lst = []
for i in range(n - 1):
    a, b = xy[i]
    for j in range(i + 1, n):
        xt, yt = xy[j]
        lst.append([a - xt, b - yt])
lst.sort()
cnt = 1
temp = 1
for i in range(len(lst) - 1):
    if lst[i] != [0, 0] and lst[i] == lst[i + 1]:
        temp += 1
        cnt = max(cnt, temp)
    else:
        temp = 1
print(max(1, n - cnt))
