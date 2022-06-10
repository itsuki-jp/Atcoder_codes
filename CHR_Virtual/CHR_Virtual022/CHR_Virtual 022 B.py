s = input()
now = []
for i in s:
    if i == "0":
        now.append("0")
    elif i == "1":
        now.append("1")
    else:
        if len(now) == 0:
            continue
        else:
            now.pop()
print(*now, sep="")
