from collections import deque


def bfs( start, w ):
    work = deque([])
    visited = set()
    work.append(start)
    visited.add(start)
    cnt = 1
    while work:
        here = work.popleft()
        for i, node in enumerate(w[here]):
            if node not in visited:
                work.append(node)
                visited.add(node)
                cnt += 1
    return cnt


n, m = map(int, input().split())
lst = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    lst[a-1].append(b-1)
ans = 0
for i in range(n):
    ans += bfs(i, lst)
print(ans)
