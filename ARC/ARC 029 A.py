n = int(input())
t = [int(input()) for _ in range(n)]
a, b = 0, 0
t.sort(reverse=True)
for i in t:
    if a > b:
        b += i
    else:
        a += i
print(max(a, b))