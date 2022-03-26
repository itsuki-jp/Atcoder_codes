n, r = map(int, input().split())
s = list(input())
if "." not in s:
    exit(print(0))

ans = 0
last = max(n - s[::-1].index(".") - r, 0)
for i in reversed(range(n)):
    if s[i] == ".":
        for j in range(max(0, i - r + 1), i + 1):
            s[j] = "-"
        ans += 1
print(ans + last)
