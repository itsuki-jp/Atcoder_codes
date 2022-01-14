n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
diff = set()
for i in range(n - 1):
    diff.add(a[i + 1] - a[i])
print(diff)