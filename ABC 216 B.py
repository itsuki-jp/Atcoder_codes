n = int(input())
lst = []
lst2 = [[] for _ in range(1001)]
cnt = 0
for _ in range(n):
    s,t = input().split()
    if s in lst:
        pos = lst.index(s)
        if t in lst2[pos]:
            print("Yes")
            exit()
        else:
            lst2[pos].append(t)
    else:
        lst.append(s)
        lst2[cnt].append(t)
        cnt += 1
print("No")


