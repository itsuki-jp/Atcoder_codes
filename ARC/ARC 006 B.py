n, l = map(int, input().split())
amida = [list(input()) for _ in range(l)]
goal = list(input())
pos = goal.index("o")

for i in range(l):
    if pos + 2 <= len(amida[0]) and amida[l - 1 - i][pos + 1] == "-":
        pos += 2
    elif 2 <= pos and amida[l - 1 - i][pos - 1] == "-":
        pos -= 2
print(pos // 2 + 1)
