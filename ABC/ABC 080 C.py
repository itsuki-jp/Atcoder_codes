n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]
ans = -1 * 10 ** 10
for i in range(1, 2 ** 10):  # 全探索
    ans_temp = 0
    for j in range(n):  # 各店ごとに
        c = 0
        for k in range(10):  # 各時間ごと
            if i >> k & 1 and f[j][k] == 1:  # フラグ立ってる and その曜日・時間に営業中
                c += 1
        ans_temp += p[j][c]
    ans = max(ans, ans_temp)
print(ans)
