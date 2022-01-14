s = input()
ans = 0
for i in range(len(s)):
    if int(i) %2 == 0:
       ans += int(s[i])
    else:
        ans -= int(s[i])
print(ans)
print()