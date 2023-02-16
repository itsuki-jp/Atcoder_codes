import sys

input = sys.stdin.readline
n = int(input())
dct = {}
for _ in range(n):
    s = input().rstrip()
    if s in dct:
        print(f"{s}({dct[s]})")
        dct[s] += 1
    else:
        print(s)
        dct[s] = 1
