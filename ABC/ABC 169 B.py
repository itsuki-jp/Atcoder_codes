n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
if a[n-1] == 0:
    print("0")
    exit()
ans = 1
for i in a:
    ans *= i
    if ans > 10 ** 18:
        ans = -1
        break
if ans > 10*18:
    ans = -1
print(ans)