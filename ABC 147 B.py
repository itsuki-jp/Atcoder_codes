s = input()
s_reverse = s[::-1]
if len(s) %2 ==0:
    n=len(s)//2
else:
    n = len(s)//2 +1

ans = 0
for i in range(n):
    if s[i] != s_reverse[i]:
        ans+=1
print(ans)