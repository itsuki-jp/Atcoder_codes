n, q = map(int, input().split())
lst = [[0, 0] for _ in range(n + 1)]
for _ in range(q):
    query = input().split()
    if query[0] == "1":
        x, y = int(query[1]), int(query[2])
        lst[x][1] = y
        lst[y][0] = x
    elif query[0] == "2":
        x, y = int(query[1]), int(query[2])
        lst[x][1] = 0
        lst[y][0] = 0
    else:
        x = int(query[1])
        ans = [x]
        now = x
        while True:
            if lst[now][0] == 0:
                break
            ans.append(lst[now][0])
            now = lst[now][0]
        ans = ans[::-1]
        now = x
        while True:
            if lst[now][1] == 0:
                break
            ans.append(lst[now][1])
            now = lst[now][1]
        print(len(ans),*ans)

