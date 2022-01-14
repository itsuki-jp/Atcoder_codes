h,w,c = map(int,input().split())
a = [list(map(int,input())) for _ in range(h)]
ans = float("inf")
for i in range(h):
    for j in range(w):
        temp = a[i][j] + c * abs()
