n = int(input())
a = list(map(int, input().split()))
a = sorted(list(set(a)),reverse=True)
if len(a) == 1:
    ans = 0
else:
    ans = 1
for i in range(len(a)):
    for j in range(len(a)-1,i,-1):
        if j == i+1:
            if a[i] // a[j] != a[i] / a[j]:
                ans += 1
                break
        if a[i] // a[j] != a[i] / a[j]:
            continue
        else:
            break
print(ans)
