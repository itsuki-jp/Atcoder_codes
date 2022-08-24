h1, w1 = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h1)]
h2, w2 = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h2)]
for i in range(2 ** (h1 + w1)):
    a_cp = []
    # 上・右から消していくと、インデックスキモくなるから、下・左から消していく
    for j in range(h1 + w1):
        if (i >> j) & 1:
            if j < h1:
                a_cp.insert(0, a[h1 - j - 1][::])
            else:
                for k in range(len(a_cp)):
                    a_cp[k].pop(w1 - (j - h1) - 1)
    if h2 == len(a_cp) and w2 == len(a_cp[0]):
        TF = True
        for y in range(h2):
            for x in range(w2):
                if a_cp[y][x] != b[y][x]:
                    TF = False
                    break
        if TF:
            print("Yes")
            break
else:
    print("No")
