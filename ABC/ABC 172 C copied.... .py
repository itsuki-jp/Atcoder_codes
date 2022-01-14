n,m,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
a_list = [0]
b_list = [0]
for i in range(n):
    a_list.append(a[i] + a_list[i])
for i in range(m):
    b_list.append(b[i] + b_list[i])

ans = 0
num = m
for i in range(n+1):
    if a_list[i] > k:
        break
    while b_list[num] > k - a_list[i]:
        num -= 1
    ans = max(ans,i + num)
print(ans)
