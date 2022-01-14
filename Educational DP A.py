n = int(input())
h = list(map(int, input().split()))
lst = [float("inf")] * (n + 3)
lst[0] = 0
for i in range(1, n):
    lst[i] = min(lst[i], lst[i - 1] + abs(h[i] - h[i - 1]))
    if i > 1:
        lst[i] = min(lst[i], lst[i - 2] + abs(h[i] - h[i - 2]))
print(lst[n - 1])


n = int(input())
h = list(map(int, input().split())) + [0,0,0]
lst = [float("inf")] * (n + 3)
lst[0] = 0
for i in range(1, n):
    lst[i + 1] = min(lst[i+1], lst[i] + abs(h[i] - h[i + 1]))
    lst[i + 2] = min(lst[i + 2], lst[i] + abs(h[i] - h[i + 2]))
print(lst[n - 1])
