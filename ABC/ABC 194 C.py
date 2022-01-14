n = int(input())
A = list(map(int,input().split()))
ans = (n-1)*A[-1]**2
lst = [0]
total = 1
for i in range(n-1):
    temp1 = (n-1)*A[i]**2
    ans += temp1
    lst.append(lst[i] + A[i])
    temp2 = 2 * lst[i+1] * A[i+1]
    ans -= temp2
print(ans)