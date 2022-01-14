a, b, n = map(int, input().split())
before = 0
for cnt in range(1,n+1,1):
    now = int((a * cnt) / b) - (a * int((cnt / b)))
    if before > now:
        print(before)
        exit()
print(now)