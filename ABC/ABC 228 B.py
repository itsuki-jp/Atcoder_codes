n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = [0 for _ in range(n + 1)]
while True:
    if ans[x - 1] == 0:
        ans[x - 1] = 1
        x = a[x - 1]
    else:
        break
print(sum(ans))
