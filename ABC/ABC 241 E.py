n, k = map(int, input().split())
a = list(map(int, input().split()))
x = 0
cnt = {}  # {あまり : i}
lst = []  # i番目のxの値
for i in range(k):
    rem = x % n
    if rem in cnt:
        rem_pst = cnt[rem]
        cycle = x - lst[rem_pst]
        size = i - rem_pst
        ans = lst[rem_pst] + (k - rem_pst) // (i - rem_pst) * cycle
        now = rem_pst + (k - rem_pst) // size * size
        for j in range(now, k):
            ans += a[ans % n]
        exit(print(ans))
    cnt[rem] = i
    lst.append(x)
    x += a[x % n]
print(x)
