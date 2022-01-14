n = int(input())
ab = [list(map(int,input().split())) for _ in range(n)]
ab = sorted(ab, key=lambda x: x[1])
now = 0
for i in ab:
    if now + i[0] <= i[1]:
        now += i[0]
    else:
        print("No")
        exit()
print("Yes")