n, x = map(int, input().split())
alp = " abcdefghijklmnopqrstuvwxyz"
for _ in alp:
    if x <= 0:
        print(_)
        break
    x -= n