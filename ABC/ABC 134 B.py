n, d = map(int, input().split())

ans = n / (2 * d + 1)
if ans == int(ans):
    print(int(ans))
    exit()
else:
    print(int(ans) + 1)
    exit()
