sd = input()
t = input()
n = len(sd)
m = len(t)
ans = list("UNRESTORABLE")
for i in range(n - m, -1, -1):
    TF = True
    temp = list(sd)
    for j in range(m):
        if sd[i + j] != "?" and sd[i + j] != t[j]:
            TF = False
            break
        temp[i + j] = t[j]
    if TF:
        ans = temp
        break
for i in ans:
    if i == "?":
        print("a", end="")
    else:
        print(i, end="")
