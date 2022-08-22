from itertools import accumulate

v_max = int(input())
n = int(input())
amount = [0 for _ in range(12 * 60)]
cnt = [0 for _ in range(12 * 60)]
for _ in range(n):
    tv = list(map(int, input().split()))
    t = tv[0]
    v = tv[1:]
    for i in range(12):
        amount[min(60 * i + t, 719)] += v[i]
        amount[min(60 * (i + 1) + t, 719)] -= v[i]
        t1 = min(60 * i + t, 719)
        t2 = min(60 * (i + 1) + t, 719)
        cnt[t1] += 1
        cnt[t2] -= 1
amount = list(accumulate(amount))
cnt = list(accumulate(cnt))

for i in range(12 * 60):
    if cnt[i] == 0:
        continue
    if v_max < amount[i]:
        print(i)
        exit()
print("No need!")
