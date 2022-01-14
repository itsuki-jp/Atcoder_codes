import itertools
n = int(input())
x = []
y = []
for i in range(n):
    x_temp,y_temp = map(int,input().split())
    x.append(x_temp)
    y.append(y_temp)

all = list(itertools.combinations([i for i in range(n)], 2))

ans = 0

for i in all:
    if -1 <= (y[i[0]] -y[i[1]])/(x[i[0]] -x[i[1]]) <= 1:
        ans += 1
print(ans)