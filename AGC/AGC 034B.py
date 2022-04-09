s = input()
s = s.replace("BC", "X")
s = s.replace("B", "-")
s = s.replace("C", "-")
s = s.split("-")
ans = 0
for i in s:
    if len(i) == 0:
        continue
    cnt = 0
    for j in reversed(range(len(i))):
        if i[j] == "X":
            cnt += 1
        else:
            ans += cnt
print(ans)