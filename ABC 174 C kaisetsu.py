k = int(input())
ans = 1
cnt = 7
for i in range(1, k + 10):
    if cnt % k == 0:
        print(i)
        exit()
    cnt = (cnt * 10 + 7) % k
print(-1)
