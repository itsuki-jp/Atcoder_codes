n = int(input())
a = list(map(int, input().split()))
lst = [0 for _ in range(200)]
for ai in a:
    lst[ai % 200] += 1
ans = 0
for i in lst:
    if i <= 1:
        continue
    ans += i * (i - 1) // 2
print(ans)