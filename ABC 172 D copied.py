n = int(input())
ans = 0
for i in range(1,n+1):
    ans += 0.5 * int(n/i) * (2 * i + (int(n/i) - 1) * i)
print(int(ans))