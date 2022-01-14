n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
# s,tの中身の数字が全く同じ(一種類の数字からなる)
if t.count(0) == s.count(0) == 0 or t.count(1) == s.count(1) == 0:
    exit(print(m))
# sが一種類からなるけど、tが2種類
if s.count(1) == 0 or s.count(0) == 0:
    exit(print(-1))

val = 10 ** 9  # シフトする回数を決める
for i in range(1, n):
    if s[i] != s[0]:
        val = min(val, min(i, n - i))
# tが一種類の文字からなる場合
if t.count(0) == 0 or t.count(1) == 0:
    if s[0] == t[0]:  # t[0]とs[0]が同じ場合は、m回足すだけでいい
        exit(print(m))
    else:  # 違う場合は、一回シフトして、後は足すだけ
        exit(print(val + m))

ans = val
if s[0] != t[0]:
    ans += 1
for i in range(1, m):
    if t[i] != t[i - 1]:
        ans += 1
    ans += 1
print(ans)
