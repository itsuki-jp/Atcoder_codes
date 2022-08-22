n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))
while q != 0:
    for li in l:
        if q == 0:
            break
        q -= 1
        pos = li - 1
        if a[pos] == n:
            continue
        if pos != (k - 1) and (a[pos] + 1) == a[pos + 1]:
            continue
        a[pos] += 1
print(*a)
