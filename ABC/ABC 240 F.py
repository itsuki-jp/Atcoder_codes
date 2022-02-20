from itertools import accumulate

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    C = []
    for __ in range(n):
        x, y = map(int, input().split())
        C .append(x * y)
    B = accumulate(C)
    A = accumulate(B)
    print(max(A))
