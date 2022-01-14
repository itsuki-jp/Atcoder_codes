# 超解説AC
def change2set( lst1 ):
    sets = set()
    for i in range(n):
        for j in range(n):
            if lst1[i][j] == "#":
                sets.add((i, j))
    return sets


n = int(input())
s = [input() for _ in range(n)]
t = [input() for _ in range(n)]
S = change2set(s)
T = change2set(t)
for _ in range(4):
    s_x, s_y = min(S)
    S = set((x - s_x, y - s_y) for x, y in S)
    t_x, t_y = min(T)
    T = set((x - t_x, y - t_y) for x, y in T)
    if S == T:
        exit(print("Yes"))
    S = set((y, -x) for x, y in S)
print("No")
