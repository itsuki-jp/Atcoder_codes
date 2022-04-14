n = int(input())
lst = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append((-a - b, a, b))
lst.sort()
ans = 0
for _ in range(n):
    ab, a, b = lst[_]
    if _ % 2 == 0:
        ans += a
    else:
        ans -= b
print(ans)
