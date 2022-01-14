
s = list(input())
t = []
n = len(s)
TF = False
for i in range(n):
    if TF:
        if s[i] == "R":
            TF = False
        else:
            if len(t) != 0 and t[0] == s[i]:
                del t[0]
            else:
                t.insert(0, s[i])
    else:
        if s[i] == "R":
            TF = True
        else:
            if len(t) != 0 and s[i] == t[-1]:
                t.pop()
            else:
                t.append(s[i])
if TF:
    print(*t[::-1], sep="")
else:
    print(*t, sep="")
