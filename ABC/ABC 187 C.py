n = int(input())
s = [input() for _ in range(n)]
ans = "satisfiable"

lst = set()
for i in s:
    temp = i
    if "!" in temp:
        if temp[1:] in lst:
            exit(print(temp[1:]))
        else:
            lst.add(temp)
    else:
        if str("!"+temp) in lst:
            exit(print(temp))
        else:
            lst.add(temp)
print(ans)