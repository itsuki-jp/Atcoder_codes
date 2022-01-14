k = int(input())
ans = 0
for i in range(1,k+1):
    for j in range(1,k+1):
        c = k/(i*j)
        if c >= 1:
            ans += int(c)
        else:
            break
print(ans)