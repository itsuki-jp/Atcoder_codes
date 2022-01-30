h, n = map(int, input().split())
ab = []  # 攻撃力、消費MP
for _ in range(n):
    a, b = map(int, input().split())
    temp = [a, b, a / b]
    ab.append(temp)
ab.sort()
print(ab)