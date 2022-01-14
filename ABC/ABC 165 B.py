import math
goal = int(input())
cnt = 0
money = 100
while goal > money:
    money = math.floor(money * 1.01)
    cnt +=1
print(cnt)