s = input()
ans = 0
for i in range(10 ** 4):
    num = str(i)
    while len(num) != 4:
        num = "0" + num
    TF = True
    for j in range(10):
        if s[j] == "o" and str(j) in num:
            continue
        if s[j] == "?":
            continue
        if s[j] == "x" and str(j) not in num:
            continue
        TF = False
    if TF:
        ans += 1
print(ans)
