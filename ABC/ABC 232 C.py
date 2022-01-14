import itertools

n, m = map(int, input().split())
ab = [[] for _ in range(n + 1)]
cd = [[] for _ in range(n + 1)]
lst = [_ for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    ab[a].append(b)
    ab[b].append(a)
for _ in range(m):
    c, d = map(int, input().split())
    cd[c].append(d)
    cd[d].append(c)
for now in itertools.permutations(lst[1:]):
    d = dict()
    for _ in range(n):
        d[_ + 1] = now[_]
    now = list(now)
    TF = True
    for i in range(n):
        if len(ab[i + 1]) != len(cd[now[i]]):
            TF = False
            break
        for j in range(len(ab[i + 1])):
            if d[ab[i + 1][j]] not in cd[now[i]]:
                TF = False
                break
    if TF:
        print("Yes")
        exit()
print("No")
