n = int(input())
a = list(map(int, input().split()))
lst = [0] * n
for i in range(n):
    lst[i] = lst[i - 1] + a[i]
ans = float("inf")
for i in range(n-1):
    n1 = lst[i]
    n2 = lst[n-1] - lst[i]
    ans = min(abs(n1 - n2), ans)
print(ans)
