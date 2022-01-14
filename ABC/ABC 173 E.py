n,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse=True)
mod = 10**9 + 7
ans = 1
cnt = 0
while cnt > k:
    if a[cnt] != 0:
        ans = (ans * a[cnt] % mod)
        cnt += 1
print(ans)