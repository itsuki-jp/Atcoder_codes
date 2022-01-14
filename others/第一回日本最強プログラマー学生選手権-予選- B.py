n,k = map(int,input().split())
a = list(map(int,input().split()))
mod = 10 ** 9 + 7
lst = [0] * n
for i in range(n):
    for j in range(i + 1,n):
        if a[i] > a[j]:
            lst[i] += 1
last = 0
for i in range(n):
    if a[-1] > a[i]:
        last += 1
num = n * (n + 1) / 2
ans = 0
for i in lst[:n - 1]:
    ans = (ans + i * num) % mod
ans = ans + (num - k) * last
print(ans % mod)