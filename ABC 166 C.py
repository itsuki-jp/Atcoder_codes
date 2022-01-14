n, m = map(int, input().split())
h = list(map(int, input().split()))
list1 = [1] * n
for _ in range(m):
    a, b = map(int, input().split())
    if h[a - 1] <= h[b - 1]:
        list1[a - 1] = 0
    if h[a - 1] >= h[b - 1]:
        list1[b - 1] = 0
print(sum(list1))