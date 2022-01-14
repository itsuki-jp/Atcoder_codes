n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if n == 1:
    print(b[0]-a[0]+1)
    exit()
ok = []
for i in range(n):
    A,B = a[i],b[i]
    temp = [i for i in range(A,B+1)]
    ok.append(temp)
ans = 0
for i in range(1,1001):
    for j in ok:
        if i not in j:
            break
    else:
        ans += 1
print(ans)