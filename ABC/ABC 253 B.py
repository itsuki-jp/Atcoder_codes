h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
pos = []
for i in range(h):
    for _ in range(3):
        if "o" in s[i]:
            if len(pos) == 0:
                pos = [i, s[i].index("o")]
            else:
                print(abs(pos[0] - i) + abs(pos[1] - s[i].index("o")))
                exit()
            s[i][s[i].index("o")] = "-"
