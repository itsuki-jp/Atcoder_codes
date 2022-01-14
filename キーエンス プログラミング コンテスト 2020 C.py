n, k, s = map(int, input().split())
if s == 10 ** 9:
    print(*[str(10 ** 9)] * k + [str(1)] * (n - k), sep=" ")
else:
    print(*[str(s)] * k + [str(s + 1)] * (n - k), sep=" ")
