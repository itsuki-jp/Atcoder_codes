# 解説AC
s = input()
n = len(s)
lst1 = [0] * (n + 1)
lst2 = [0] * (n + 1)
for i in range(n):
    if s[i] == "<":
        lst1[i + 1] = lst1[i] + 1
s = s[::-1]
for i in range(n):
    if s[i] == ">":
        lst2[i + 1] = lst2[i] + 1
ans = 0
lst2 = lst2[::-1]
for i in range(n + 1):
    ans += max(lst1[i], lst2[i])
print(ans)
