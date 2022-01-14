n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
lst = [0] * n
ans = 0
for i in range(n):
    if i < k:
        if t[i] == "r":
            ans += p
            lst[i] = "p"
        if t[i] == "s":
            ans += r
            lst[i] = "r"
        if t[i] == "p":
            ans += s
            lst[i] = "s"
    else:
        if t[i] == "r":
            if lst[i - k] == "p":
                lst[i] = "a"
            else:
                ans += p
                lst[i] = "p"
        if t[i] == "s":
            if lst[i - k] == "r":
                lst[i] = "a"
            else:
                ans += r
                lst[i] = "r"
        if t[i] == "p":
            if lst[i - k] == "s":
                lst[i] = "a"
            else:
                ans += s
                lst[i] = "s"
print(ans)
