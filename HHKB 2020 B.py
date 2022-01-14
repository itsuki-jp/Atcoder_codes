h,w = map(int,input().split())
s = [input() for _ in range(h)]
ans = 0

for i in range(h):
    t = s[i].split("#")
    for j in t:
        if len(j) >= 2:
            ans += (len(j)-1)
s = [list(x) for x in zip(*s)]
for i in range(w):
    t = "".join(s[i])
    t = t.split("#")
    for j in t:
        if len(j) >= 2:
            ans += (len(j)-1)
print(ans)