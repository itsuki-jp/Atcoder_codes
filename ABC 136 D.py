s = input()
n = len(s)
lst = [0] * n
num = 0
for i in range(n):
    if s[i] == "L":
        if num % 2 == 0:
            lst[i] += num // 2
            lst[i - 1] += num // 2
        else:
            lst[i] += num // 2
            lst[i - 1] += num // 2 + 1
        num = -1
    num += 1
num = 0
for i in range(n - 1, -1, -1):
    if s[i] == "R":
        if num % 2 == 0:
            lst[i] += num // 2
            lst[i + 1] += num // 2
        else:
            lst[i] += num // 2
            lst[i + 1] += num // 2 + 1
        num = -1
    num += 1
print(*lst)
