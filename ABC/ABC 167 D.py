n,k = map(int,input().split())
a = list(map(int,input().split()))
path = [1]
pos = 1
for i in range(k-1):
    pos = a[pos-1]
    if pos in path:
        num2 = path.index(pos)
        if num2 == path.index((a[pos-1])) -1:
            num = len(path[num2:])
            x,y = divmod(k +1 -len(path) + num ,num)
            if x>1:
                path = path[num2:]
                if y ==0:
                    print(path[-1])
                else:
                    print(path[y-1])
            else:
                print(pos)
            exit()
    else:
        path.append(pos)
print(pos)
