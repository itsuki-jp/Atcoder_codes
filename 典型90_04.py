h,w = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]
tate = [0] * w
for i in range(h):
    for j in range(w):
        tate[j] += a[i][j]
yoko = [sum(i) for i in a]
for i in range(h):
    for j in range(w):
        print(tate[j] + yoko[i] - a[i][j],end=" ")
    print()