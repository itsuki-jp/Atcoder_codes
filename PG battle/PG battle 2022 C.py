n, m = map(int, input().split())
s = [int(_) for _ in input()]
t = [int(_) for _ in input()]
k = int(input())
for _ in range(k):
    y, x = map(int, input().split())
    if y == x == 1:
        print(s[0])
    elif y == 1:
        print(t[x - 1])
    elif x == 1:
        print(s[y - 1])
    else:
        ans = s[1]
        for i in range(2, y):
            ans ^= s[i]
        for i in range(1, x):
            ans ^= t[i]
        print(ans)
