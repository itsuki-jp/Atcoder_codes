n = int(input())
ans = [0] * n+1

for x in range(1,32):
    for y in range(1,32):
        for z in range(1,32):
            temp = x**2 + y**2 + z**2 +x*y + y*z + z*x
            if 1 <= temp <= n:
                ans[temp] += 1
