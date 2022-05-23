n = int(input())
d = {}
ans = []
for i in range(n):
    s, t = input().split()
    if s in d:
        continue
    d[s] = True
    ans.append((-int(t), i))
ans.sort()
print(ans[0][1] + 1)
