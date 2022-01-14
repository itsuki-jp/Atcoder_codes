n, m, x = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(n)]
price = []
for i in range(2 ** n):
    cnt = [0]*m
    price_temp = 0
    for j in range(n):
        if (i >> j) & 1:
            price_temp += c[j][0]
            for k in range(m):
                cnt[k] += c[j][k+1]
    if all(s >= x for s in cnt):
        price.append(price_temp)
print(min(price) if len(price) > 0 else -1)