S = input()[::-1]
ans = 0
num = 0
for i in range(len(S)):
    if S[i] == "B":
        ans += (i - num)
        num += 1
print(ans)