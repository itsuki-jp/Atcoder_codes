from collections import deque

q = int(input())
d = deque()
for _ in range(q):
    t = input().split()
    if t[0] == "1":
        x, c = map(int, t[1:])  # 値、個数
        d.append((x, c))
    else:
        c = int(t[1])  # 個数
        total = 0
        while True:
            if c <= 0:
                break
            a, b = d.popleft()
            if b <= c:
                total += a * b
                c -= b
            else:
                total += c * a
                d.appendleft((a, b - c))
                c = 0
        print(total)
