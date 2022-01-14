n, m = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]
lst = [(b[0][0] + i) for i in range(m)]
for i in range(n):
    if b[i] != lst:
        exit(print("No"))
    temp = lst[0]
    lst = [(7 + temp + i) for i in range(m)]
exit(print("Yes"))
