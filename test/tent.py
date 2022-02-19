n, m = map(int, input().split())
py = []
dct = {}
for _ in range(m):
    p_t, y_t = map(int, input().split())
    dct[(p_t, y_t)] = _
    dct[_] = (p_t, y_t)
    py.append((p_t, y_t))
py_sorted = sorted(py)
ans = dict()
temp = 0
pre = -1
for p, y in py_sorted:
    if pre == p:
        temp += 1
    else:
        temp = 1
    ans[(p, y)] = temp
    pre = p
for i in py:
    print(f"{str(i[0]).zfill(6)}{str(ans[i]).zfill(6)}")