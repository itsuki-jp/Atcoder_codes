s = list(input())
n = len(s)
k = int(input())
ans = 0
x = 0
cnt = 0
j = 0
for i in range(n):
    while j != n and (cnt != k or s[j] == "X"):
        if s[j] == ".":
            cnt += 1
        else:
            x += 1
        j += 1
    ans = max(ans, cnt + x)
    if s[i] == ".":
        cnt -= 1
    else:
        x -= 1
print(ans)
