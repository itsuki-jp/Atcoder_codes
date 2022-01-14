n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
acc = [t[0]] + [0] * n
for i in range(1, n):
    if t[i] > acc[i - 1] + s[i - 1]:
        acc[i] = acc[i - 1] + s[i - 1]
    else:
        acc[i] = t[i]

acc = acc[:n]
if acc[0] > acc[-1] + s[-1]:
    acc[0] = acc[-1] + s[-1]

for i in range(1, n):
    if acc[i] > acc[i - 1] + s[i - 1]:
        acc[i] = acc[i - 1] + s[i - 1]
print(*acc, sep="\n")
