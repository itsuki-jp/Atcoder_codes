n, k = map(int, input().split())
ans = min(n % k, -n % k)
print(ans)
