n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n - 1):
    if (abs(a[i] - a[i + 1]) <= k and abs(a[i] - b[i + 1]) <= k) or (abs(b[i] - a[i + 1]) <= k and abs(b[i] - b[i + 1]) <= k):
        continue
    else:
        exit(print("No"))
print("Yes")
