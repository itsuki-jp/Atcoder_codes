a, b, c = map(int, input().split())
ans = 0
for i in range(1000):
    if len(set(a, b, c)) == 1:
        print(ans)
        exit()
