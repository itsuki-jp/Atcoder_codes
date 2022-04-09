h, n = map(int, input().split())
ab = []  # 攻撃力、消費MP
for _ in range(n):
    at, bt = map(int, input().split())
    temp = [-at / bt, -at, bt]
    ab.append(temp)
ab.sort()
ans = float("inf")
temp = 0
for i in range(n):
    if h < 0:
        break
    r, a, b = ab[i]
    a *= -1
    if h % a == 0:  # 魔法を使うとちょうど倒せる時
        ans = min(ans, temp + b * (h // a))
        break
    else:
        ans = min(ans, temp + b * ((h + a - 1) // a))   # Overpowered
        temp += b * (h // a)  # 敵のHPが残るように魔法を使った場合
        h -= (h // a) * a
print(ans)
