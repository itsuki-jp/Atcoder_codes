n = int(input())
a = ["".join(set(input())) for _ in range(n)]
ans = str()
for i in range(n//2):
    for j in range(n):
        if a[i][j] in a[n-i-1]:
            ans += a[i][j]
            break
mid = str()
if n//2 != n/2:
    mid= str(a[n//2][0])
ans =ans + mid + ans[::-1]
if len(ans) == n:
    print(ans)
else:
    print(-1)
