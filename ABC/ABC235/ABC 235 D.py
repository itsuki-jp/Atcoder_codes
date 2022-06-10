from collections import deque

a, n = map(int, input().split())
d = deque()
d.append((1, 0))
TF = False
x = -1
sets = set()
while d:
    x, cnt = d.popleft()
    if x in sets:
        continue
    sets.add(x)
    if x == n:
        TF = True
        break
    if x >= 10 and x % 10 != 0:
        temp = str(x)
        temp = temp[-1] + temp[:len(temp) - 1]
        temp = int(temp)
        d.append((temp, cnt + 1))
    if not x * a > 10 * n:
        d.append((x * a, cnt + 1))
if TF:
    print(cnt)
else:
    print(-1)
