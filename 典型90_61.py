from collections import deque
q = int(input())
queue = deque()
for _ in range(q):
        t,x = map(int,input().split())
        if t == 1:
            queue.appendleft(x)
        elif t == 2:
            queue.append(x)
        else:
            print(queue[x-1])