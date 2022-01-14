n,p = map(int, input().split())
ans = 0
a = list(map(int, input().split()))
for i in a:
    if i < p:
        ans += 1
print(ans)