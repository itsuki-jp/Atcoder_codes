s = input()
t = input()
alp = "abcdefghijklmnopqrstuvwxyz" * 10
k = alp.index(t[0]) - alp.index(s[0])
if k < 0:
    k += 26
ans = "Yes"
for i in range(len(t)):
    if t[i] == alp[k + alp.index(s[i])]:
        continue
    exit(print("No"))
print(ans)
