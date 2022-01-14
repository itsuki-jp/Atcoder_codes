t, n = map(int, input().split())
a = -(-100 * n // t)  # 切り上げの割り算
ans = (100 + t) * a // 100 - 1
print(ans)

# https://zenn.dev/m193h/articles/20210510mon011626m193harc118
