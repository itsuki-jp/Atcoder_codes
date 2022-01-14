n = int(input())
a = [input() for _ in range(n)]
# 横から読む
for i in a:
    if i == i[::-1]:
        print(i)
        exit()
# 横と縦を交換
a = list(zip(*a))
new = []
for j in a:
    s = "".join(j)
    new.append(s)
# 横から読む
for k in new:
    if k == k[::-1]:
        print(k)
        exit()
print(-1)
