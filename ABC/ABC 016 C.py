n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
for i in range(n):
    start = set(graph[i])
    start.add(i)
    goal = set()
    for j in graph[i]:
        goal |= set(graph[j])
    ans = goal - start
    print(len(ans))

