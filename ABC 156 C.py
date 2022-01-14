n = int(input())
x = list(map(int, input().split()))
if min(x) == max(x):
    print(0)
    exit()

dist_min = 9999999999999
for i in range(min(x),max(x)):
    dist_sum = 0
    for j in range(n):
        dist_sum += (x[j] - i)**2
    if dist_sum < dist_min:
        dist_min = dist_sum

print(dist_min)