import sys
from collections import deque


def test():
    lines = []
    with open("input05.txt") as f:
        for s_line in f:
            lines.append(s_line.rstrip('\r\n'))
    return lines


def real():
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    return lines


def search_index( alp, graph ):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == alp:
                return i, j


def main( lines ):
    n, m = map(int, lines[0].split())
    s = [list(lines[_ + 1]) for _ in range(n)]
    info = [[[10 ** 5, 10 ** 5] for _ in range(m)] for _ in range(n)]  # cost, cnt
    start = search_index("S", s)
    s[start[0]][start[1]] = (0, 0)
    goal = search_index("G", s)
    d = deque()
    d.append((start, 0, 0))  # [y,x], cost, cnt
    while d:
        pos, cost, cnt = d.popleft()
        for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny = pos[0] + dy
            nx = pos[1] + dx
            if not (0 <= nx < m) or not (0 <= ny < n):
                continue
            n_cost = cost + 1
            n_cnt = cnt
            if s[ny][nx] == "#":
                n_cost += cnt
                n_cnt += 1
            if info[ny][nx][0] > n_cost:
                info[ny][nx] = [n_cost, n_cnt]
                d.append(([ny, nx], n_cost, n_cnt))
    print(info[goal[0]][goal[1]][0])


if __name__ == '__main__':
    main(real())
