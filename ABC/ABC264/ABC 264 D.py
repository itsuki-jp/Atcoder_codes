from collections import deque

s = list(input())
d = deque()
sets = set()
d.append((s, 0))
while d:
    ss, cnt = d.popleft()
    temp = "".join(ss)
    if temp in sets:
        continue
    sets.add(temp)
    if temp == "atcoder":
        print(cnt)
        break
    for i in range(len(temp) - 1):
        temp2 = ss[::]
        temp2[i], temp2[i + 1] = temp2[i + 1], temp2[i]
        d.append((temp2, cnt + 1))
