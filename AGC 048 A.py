n = int(input())
ss = [list(input()) for _ in range(n)]
atcoder = list("atcoder")
for s in ss:
    now = 1
    count = 0
    while True:
        if atcoder > s:
            if now == 0 or now == len(s):
                print(-1)
                break
            if s[now] != "a":
                s[now], s[now - 1] = s[now - 1], s[now]
                now -= 1
                count += 1
            else:
                now += 1
        else:
            print(count)
            break
