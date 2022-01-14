n = int(input())
x = []
y = []
xy_sum = []
for i in range(n):
    x_temp, y_temp = map(int, input().split())
    x.append(x_temp)
    y.append(y_temp)
    xy_sum.append([2 * x_temp + y_temp, x_temp, y_temp])
sum_x = sum(x)
sum_y = 0
xy_sum.sort(reverse=True)
xy_sum.append([0, 0, 0])
ans = 0
for i in xy_sum:
    if sum_x < sum_y:
        exit(print(ans))
    else:
        sum_x -= i[1]
        sum_y += (i[1] + i[2])
        ans += 1
