n = int(input())
money = 0
i = 0
while True:
    if money >= n:
        print(i-1)
        exit()
    money += i
    i += 1