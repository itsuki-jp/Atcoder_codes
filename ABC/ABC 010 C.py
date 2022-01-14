xa, ya, xb, yb, t, v = map(int, input().split())
n = int(input())
if ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5 == t * v:
    print("NO")
else:
    for _ in range(n):
        x, y = list(map(int,input().split()))
        time = ((xa - x) ** 2 + (ya - y) ** 2) ** 0.5 + ((x - xb) ** 2 + (y - yb) ** 2) ** 0.5
        if time <= t * v:
            print("YES")
            exit()
print("NO")
