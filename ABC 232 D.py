def solve( x, y, cnt ):
    for nnx, nny in [[1, 0], [0, 1]]:
        nx = x + nnx
        ny = y + nny
        if not 0 <= nx < w or not 0 <= ny < h:
            continue
        if graph[ny][nx] == -1:
            continue
        if graph[ny][nx] <= cnt:
            graph[ny][nx] = cnt + 1
            solve(nx, ny, cnt + 1)


h, w = map(int, input().split())
graph = []
for _ in range(h):
    c = list(input())
    temp = []
    for __ in c:
        if __ == "#":
            temp.append(-1)
        else:
            temp.append(0)
    graph.append(temp)
graph[0][0] = 1
solve(0, 0, 1)
ans = 0
for _ in graph:
    ans = max(ans,max(_))
print(ans)
