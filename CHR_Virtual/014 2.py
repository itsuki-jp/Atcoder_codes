s = input()
ans = 0
for i in range(10 ** 4):
    now = str(i)
    ok = True
    while len(now) != 4:
        now = "0" + now
    for j in range(10):
        if s[j] == "o" and str(j) in now:
            continue
        if s[j] == "?":
            continue
        if s[j] == "x" and str(j) not in now:
            continue
        ok = False
    if ok:
        ans += 1
print(ans)