from collections import defaultdict
n, m = map(int, input().split())
a, b, c, d, e, f = map(int, input().split())
blocked = set([tuple(map(int, input().split())) for _ in range(m)])

visited_count = defaultdict(int)
