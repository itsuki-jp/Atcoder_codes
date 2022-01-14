n,k = map(int,input().split())
h = list(map(int, input().split())) + [0]*k
lst = [float("inf")] * (n + k)
lst[0] = 0
for i in range(n):
    for j in range(1,k+1):
        lst[i + j] = min(lst[i+j], lst[i] + abs(h[i] - h[i + j]))
print(lst[n - 1])