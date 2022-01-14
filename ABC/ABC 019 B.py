s = input()
s += "A"
cnt = 1
ans = []
for i in range(1,len(s)):
    if s[i-1] == s[i]:
        cnt += 1
    else:
        print(s[i-1],end="")
        print(cnt,end="")

        cnt = 1
print()