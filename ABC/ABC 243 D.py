# 解説AC
n, x = map(int, input().split())
s = input()
b = list(bin(x)[2:])
for i in s:
    if i == "L":
        b.append("0")
    elif i == "R":
        b.append("1")
    else:
        b.pop()
print(int("".join(b), 2))
