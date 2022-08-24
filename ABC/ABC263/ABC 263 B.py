n = int(input())
p = [int(_) - 1 for _ in input().split()]
pos = n - 2
ans = 1
while True:
    if p[pos] == 0:
        print(ans)
        break
    pos = p[pos] - 1
    ans += 1
