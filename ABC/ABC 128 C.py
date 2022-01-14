# 求:全ての電球が点灯するようなスイッチの on/off の状態の組み合わせ

n, m = map(int, input().split())  # スイッチ,電球
k = []
s = []
for _ in range(m):
    ks = list(map(int, input().split()))
    k.append(ks[0])
    s.append(ks[1:])
# 電球iは、ki個のスイッチのうちonになっている個数を2で割った余りがpiに等しいときに点灯する
p = list(map(int, input().split()))
ans = 0
for i in range(2 ** n):
    switch_on = [0] * n  # onになってるスイッチのリスト
    num_light = 0
    for j in range(n):
        if i >> j & 1:
            switch_on[j] = 1
    for j in range(m):  # 電球を一つづつ確認する
        num = 0
        for x in s[j]:
            if switch_on[x - 1] == 1:
                num += 1
        if num % 2 == p[j]:
            num_light += 1
    if num_light == m:
        ans += 1
print(ans)