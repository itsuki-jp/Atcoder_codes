n = int(input())

mod = 7 + 10 ** 9

ans = (10 ** n) % mod - (9 ** n) % mod - (9 ** n) % mod + (8 ** n) % mod
print(ans%mod)