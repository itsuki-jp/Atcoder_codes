n,m = map(int,input().split())
graph = [set() for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    if a > b:
        graph[a-1].add(b)
    if a < b:
        graph[b-1].add(a)
ans = 0
for i in range(n):
    if len(graph[i]) == 1:
        ans += 1
print(ans)