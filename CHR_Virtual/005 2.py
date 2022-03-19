from collections import deque

n = int(input())
s = input()
ans = deque([n])
for i in range(n):
    if s[-i - 1] == "L":
        ans.append(n - i - 1)
    else:
        ans.appendleft(n - i - 1)
print(*list(ans))
