from itertools import combinations

n, m = map(int, input().split())

for _ in list(combinations(range(1, m + 1), n)):
    print(*_)
