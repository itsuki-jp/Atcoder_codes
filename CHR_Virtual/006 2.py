a, b, k, l = map(int, input().split())
# k個以上買う, 個別だとa円, L個のセットだとB円
ans = ((k + l - 1) // l) * b
if not k % l == 0:
    ans = min(ans, k // l * b + k % l * a)
print(ans)
