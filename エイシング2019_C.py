import sys


def search( y, x ):
    for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        ny, nx = y + i, x + j
        if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx]:
            if graph[y][x] != graph[ny][nx]:
                if graph[y][x] == "#":
                    num[0] += 1
                else:
                    num[1] += 1
                visited[ny][nx] = 1
                search(ny, nx)


sys.setrecursionlimit(10 ** 6)
h, w = map(int, input().split())
graph = [input() for _ in range(h)]
visited = [[0 for _ in range(w)] for _ in range(h)]
num = [0, 0]
ans = 0
for y in range(h):
    for x in range(w):
        if visited[y][x]:
            continue
        search(y, x)
        ans += num[0] * num[1]
        num = [0, 0]
print(ans)
