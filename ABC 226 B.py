n = int(input())
sets = set()
for _ in range(n):
    a = tuple(map(int, input().split()))[1:]
    sets.add(a)
print(len(sets))