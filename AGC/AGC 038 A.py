h, w, a, b = map(int, input().split())
ans = [[0 for _ in range(w - a)] + [1 for _ in range(a)] for _ in range(b)] + [
    [1 for _ in range(w - a)] + [0 for _ in range(a)] for _ in range(h - b)]
for i in ans:
    print(*i, sep="")
