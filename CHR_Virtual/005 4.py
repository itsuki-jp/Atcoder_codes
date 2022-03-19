n = int(input())
# 同じ色なら不満は0,違ったらabs(ai-aj)
ac = []
rgb = [[] for _ in range(3)]
for _ in range(2 * n):
    at, ct = input().split()
    ac.append((int(at), ct))
    if ct == "R":
        rgb[0].append(at)
    elif ct == "G":
        rgb[1].append(at)
    else:
        rgb[2].append(at)
rgb = [sorted(_) for _ in rgb]
rem = 2 * n
ans = 0
while rem:

