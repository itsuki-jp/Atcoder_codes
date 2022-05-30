from itertools import combinations

n = int(input())
ok = "MARCH"
s = [0 for _ in range(5)]
for _ in range(n):
    t = input()
    if t[0] in ok:
        s[ok.index(t[0])] += 1
ans = 0
for i in combinations(s, 3):
    ans += i[0] * i[1] * i[2]
print(ans)
