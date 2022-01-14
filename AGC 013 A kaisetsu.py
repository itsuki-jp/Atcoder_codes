n = int(input())
s = list(map(int, input().split()))
if n == 1 or n == 2:
    exit(print(1))
same = 1
big = 0
if s[0] != s[1]:
    same = 0
    if s[0] < s[1]:
        big = 1
ans = 1
for i in range(1, n):
    if same:
        if s[i - 1] > s[i]:
            big = 0
            same = 0
        elif s[i - 1] < s[i]:
            big = 1
            same = 0
    elif big:
        if s[i - 1] > s[i]:
            ans += 1
            big = 0
            same = 1
    else:
        if s[i - 1] < s[i]:
            ans += 1
            big = 1
            same = 1
print(ans)
