from bisect import bisect_left

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(list(map(int, input().split())))

ans = float("inf")
for i in a:
    num = bisect_left(b, i)
    ans = min(ans,abs(i - b[num - 1]))
    if num < m:
        ans = min(ans, abs(i - b[num]))
print(ans)
