n = input()
l = len(n)
if int(n) % 3 == 0:
    exit(print(0))
ans = float("inf")
for i in range(2**l):
    temp = 0
    lst = "0"
    for j in range(l):
        if (i >> j) & 1:
            lst = n[j] + lst
            temp += 1
    if int(lst) != 0 and int(lst) % 3 == 0:
        ans = min(ans,l-temp)
print(ans if ans != float("inf") else -1)
