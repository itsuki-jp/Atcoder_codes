x = input()
lst = ["o", "k", "u"]
cnt = 0
while True:
    if cnt == len(x):
        print("YES")
        exit()
    temp = x[cnt:cnt+1]
    if cnt != len(x) - 2 and x[cnt:cnt + 2] == "ch":
        cnt += 2
    elif x[cnt] in lst:
        cnt += 1
    else:
        print("NO")
        exit()
