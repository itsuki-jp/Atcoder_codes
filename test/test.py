import random

lst = []
temp = True
while temp:
    temp = list(map(float, input().split(",")))
    temp[-1] = int(temp[-1]//1)
    if len(temp) == 1:
        break
    lst.append(temp)
random.shuffle(lst)
for _ in lst:
    print(*_, sep=",")
