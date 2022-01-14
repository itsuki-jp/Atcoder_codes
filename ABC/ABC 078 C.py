n, m = map(int, input().split())
ans = m * 1900 + (n - m) * 100
print(ans * 2**m)
