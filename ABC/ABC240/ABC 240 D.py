from collections import deque

n = int(input())
a = list(map(int, input().split()))
d = deque()
length = 0
for k in range(n):
    if len(d) == 0:
        length += 1
        d.append((a[k], 1))
    else:
        tf = False
        d.append((a[k], 1))
        length += 1
        while True and len(d) >= 2:
            pre = d.pop()
            prepre = d.pop()
            if pre[0] == prepre[0]:
                tf = True
                if pre[1] + prepre[1] == pre[0]:
                    length -= pre[0]
                else:
                    d.append((a[k], pre[1] + prepre[1]))
            else:
                d.append(prepre)
                d.append(pre)
                break
    print(length)
