# 解説AC
n = int(input())
a = list(map(int, input().split()))
money = 1000
stock = 0
for i in range(n - 1):
    money += stock * a[i]
    stock = 0
    if a[i] < a[i + 1]:
        stock = money // a[i]
        money -= stock * a[i]
print(money + stock * a[-1])
