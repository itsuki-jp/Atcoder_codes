from collections import deque

n = int(input())
s = input()
a = deque()
a.append(n)
for i in reversed(range(n)):
    if s[i] == "L":
        a.append(i)
    else:
        a.appendleft(i)
print(*list(a))