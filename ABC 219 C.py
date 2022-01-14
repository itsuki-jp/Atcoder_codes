x = input()
n = int(input())
s = [input() for _ in range(n)]
alp = "abcdefghijklmnopqrstuvwxyz"
ns = []
for i in range(n):
    temp = ""
    for j in s[i]:
        pos = x.index(j)
        temp += alp[pos]
    ns.append([temp, i])
ns.sort()
for i, j in ns:
    print(s[j])
