from collections import deque

X = input()
d = deque("a")
for x in X:
    pre = d.pop()
    if pre == "S" and x == "T":
        continue
    d.append(pre)
    d.append(x)
print(len(d) - 1)
