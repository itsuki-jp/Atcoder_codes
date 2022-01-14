n = int(input())
st = list(map(int, input().split()))
ans = 0
mx = 1000
for s in st:
    TF = True
    for a in range(1, mx + 1):
        if not TF:
            break
        for b in range(1, mx + 1):
            if (4 * a * b + 3 * a + 3 * b) == s:
                TF = False
                break
    if TF:
        ans += 1
print(ans)
