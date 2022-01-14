n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    if len(i) == n - 1:
        exit(print("Yes"))
print("No")
