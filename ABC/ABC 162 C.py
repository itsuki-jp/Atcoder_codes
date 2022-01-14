import math
goal = 0
n = int(input())
n+=1
for i in range(1,n):
    for j in range(1,n):
        for k in range(1,n):
            list1 = [i,j,k]
            ans = list1[0]
            for m in range(1, 3):
                ans = math.gcd(ans, list1[m])
            goal +=ans

print(goal)