n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            xi = xy[i][0]
            xj = xy[j][0]
            xk = xy[k][0]
            yi = xy[i][1]
            yj = xy[j][1]
            yk = xy[k][1]
            if (yj-yi) > 0 and (xj-xi) > 0:
                if (yk-yi)/(yj-yi) == int((yk-yi)/(yj-yi)) and (xk-xi)/(xj-xi) == int((xk-xi)/(xj-xi)):
                    print("Yes")
                    exit()
    print("No")
