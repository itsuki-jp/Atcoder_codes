s = list(input())
ans = str()
cnt = 0

while s:
    now = s.pop(0)
    if now == " ":
        if s[0] == " ":
            now = s.pop(0)
        ans = ans + ","
    else:
        ans = ans + now
print(ans)