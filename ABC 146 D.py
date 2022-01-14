def solve(now,pre_pos,pre_cl):
    for nxt in graph[now]:
        if nxt == pre_pos or ans_lst[nxt]:
            continue



n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
ans_num = -1
pos = 0
for i in range(n + 1):
    if len(graph[i]) > ans_num:
        ans_num = len(graph)
        pos = i
print(ans_num)
ans_lst = [0 for _ in range(n + 1)]
