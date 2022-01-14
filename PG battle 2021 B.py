t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    small = n - m if n > m else 1
    temp = n * (n - 1) / 2
    print(small, m - temp)
