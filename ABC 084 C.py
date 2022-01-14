from math import ceil

n = int(input())
c = [0] * n
s = [0] * n
f = [0] * n
for i in range(n - 1):
    c[i], s[i], f[i] = map(int, input().split())

for i in range(n - 1):  # スタート位置
    time = c[i] + s[i]
    for j in range(i + 1, n - 1):  # 一駅づつ移動する
        if time <= s[j]:
            time = s[j]
        else:
            temp = ceil(time / f[j]) * f[j]
            time = temp
        time += c[j]
    print(time)
print(0)
