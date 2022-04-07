n, m = map(int, input().split())
ans = min(n, m // 2)
m -= n * 2
if not m <= 0:
    ans += m // 4
print(ans)
