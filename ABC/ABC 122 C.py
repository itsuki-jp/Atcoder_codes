n, q = map(int, input().split())
s = " " + input()
lst = [0] * (n + 1)
for i in range(n):
    if s[i + 1] == "C" and s[i] == "A":
        lst[i + 1] = 1
    lst[i + 1] += lst[i]
for _ in range(q):
    l, r = map(int, input().split())
    print(lst[r] - lst[l])
