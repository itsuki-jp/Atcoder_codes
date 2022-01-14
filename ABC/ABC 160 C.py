k, n = map(int, input().split())

s = list(map(int, input().split()))
longest = 0
for i in range(n - 1):
    long = s[i + 1] - s[i]
    if long > longest:
        longest = long
if longest >= k - s[n - 1] + s[0]:
    print(k - longest)
else:
    print(s[n - 1] - s[0])