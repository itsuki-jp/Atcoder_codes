n = int(input())
c = [0] + sorted(list(map(int, input().split())))
mod = 10 ** 9 + 7
ans = 1
for i in range(1, n+1):
    ans *= (c[i] - i + 1)
    ans %= mod

print(ans)
