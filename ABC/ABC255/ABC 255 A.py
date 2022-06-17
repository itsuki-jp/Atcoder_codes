r, c = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
if r == 1:
    print(a1[c - 1])
else:
    print(a2[c - 1])
