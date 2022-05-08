n = int(input())
last = 0
for i in range(10 ** 5):
    if 2 * n <= i + i ** 2:
        last = i
        break
ans = []
now = last + 1
while n:
    now -= 1
    if n - now >= 0:
        ans.append(now)
        n -= now
print(*ans[::-1])
