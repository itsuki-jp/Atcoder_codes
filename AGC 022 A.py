s = input()
alp = "abcdefghijklmnopqrstuvwxyz"
if len(s) == 26 and s == alp[::-1]:
    print(-1)
elif len(s) == 26:
    for i in range(25,-1,-1):
        if s[i - 1] < s[i]:
            print(s[:i - 1],end="")
            for j in alp:
                if s[i - 1] < j and j not in s[:i - 1]:
                    print(j)
                    exit()
else:
    for i in alp:
        if i not in s:
            print(s + i)
            exit()