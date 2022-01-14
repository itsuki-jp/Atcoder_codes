# 解説見た
n = int(input())
b = list(map(int,input().split()))
ans = []
alp = "abcdefghijklmnopqrstuvwxyz"
for i in range(n-1,-1,-1):
    ok = []
    for j in range(i + 1):
        if b[j] == j + 1:
            ok.append(j)
    if len(ok) != 0:
        ans.append(b.pop(ok[-1]))
    else:
        ans = [-1]
        break
print(*ans[::-1],sep="\n")
