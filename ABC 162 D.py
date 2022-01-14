n = int(input())
s = list(input())

ans = s.count("R") * s.count("G") * s.count("B")

for i in range(n):
    for d in range(n):
        j = i + d
        k = i + 2 * d
        if k >= n:
            break
        if s[i] != s[j] and s[j] != s[k] and s[i] != s[k]:
            ans -= 1

print(ans)
