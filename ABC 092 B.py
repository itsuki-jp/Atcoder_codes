n = int(input())
d,x = map(int,input().split())
a = [int(input()) for _ in range(n)]
for i in range(n):
    cnt = 0
    for j in range(1000000):
        cnt = j * a[i] +1
        if cnt > d:
            break
    x += j
print(x)