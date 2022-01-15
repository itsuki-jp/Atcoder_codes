n = int(input())
h = list(map(int, input().split())) + [-10000]
now = 0
while now != n:
    if h[now] < h[now + 1]:
        now += 1
    else:
        break
print(h[now])
