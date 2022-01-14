x = int(input())
ans  = 1
for b in range(1,32):
    for p in range(2,10):
        c = b**p
        if x >= c > ans:
            ans = c
print(ans)
