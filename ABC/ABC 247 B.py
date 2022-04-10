from collections import Counter

n = int(input())
ST = [input().split() for _ in range(n)]
s = Counter([ST[_][0] for _ in range(n)] + [ST[_][1] for _ in range(n)])
for i in range(n):
    st, tt = ST[i]
    if s[tt] == 1 or s[st] == 1 or (st == tt and s[st] == 2):
        continue
    exit(print("No"))
print("Yes")
