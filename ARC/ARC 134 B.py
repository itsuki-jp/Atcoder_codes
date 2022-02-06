n = int(input())
s = input()
s_rev = s[::-1]
alp = "abcdefghijklmnopqrstuvwxyz"
lst = [[] for _ in range(26)]
for _ in range(n):
    lst[ord(s_rev[_]) - 97].append(n - _ - 1)
top = 0
last = n
trans = []
for i in lst:
    for j in i:
        while top < last and s[top] <= s[j]:
            top += 1
        if top < j < last:
            trans.append((top, j))
            top += 1
            last = j
ans = list(s)
for (x, y) in trans:
    ans[x], ans[y] = ans[y], ans[x]
print(*ans, sep="")
