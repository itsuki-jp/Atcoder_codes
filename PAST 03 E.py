n,m,q = map(int,input().split())
connection = [[] for i in range(n)]
for _ in range(m):
    u,v = map(int,input().split())
    connection[u-1].append(v)
    connection[v-1].append(u)
c = list(map(int,input().split()))
for i in range(q):
    s = list(map(int,input().split()))
    x = s[1]
    if s[0] == 1:
        print(c[x-1])
        for j in connection[x-1]:
            c[j-1] = c[x-1]

    else:
        y = s[2]
        print(c[x-1])
        c[x-1] = y
