n = int(input())
ts = []
for i in range(n):
    s, t = input().split()
    t = int(t)
    ts.append([t, s])
ts = sorted(ts)
print(ts[-2][1])
print(ts)
