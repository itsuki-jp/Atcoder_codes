s = input()
t = int(input())
x,y = 0,0
cnt = 0
for i in s:
    if i == "L":
        x -= 1
    if i == "R":
        x += 1
    if i == "U":
        y += 1
    if i == "D":
        y -= 1
    if i == "?":
        cnt += 1
ans = abs(x) + abs(y)
if t == 1:  #max
    print(ans + cnt)
else:
    min_val = ans
    for j in range(cnt):
        temp = abs(x-j) + abs(y-(cnt-j))
        if temp < min_val:
            min_val = temp
    print(min_val)