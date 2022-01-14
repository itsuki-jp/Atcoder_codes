# 存在し得る正直者の最大人数
n = int(input())
a = []
xy = []  # xが正直 -> y = 1, xが不親切-> y = 0
for _ in range(n):
    a_temp = int(input())
    a.append(a_temp)
    temp = []
    for _ in range(a_temp):
        xy_temp = list(map(int, input().split()))
        temp.append(xy_temp)
    xy.append(temp)
ans = 0
for i in range(2 ** n):
    ok = True
    TF_lst = [int(i >> k & 1) for k in range(n)]
    ans_temp = 0
    for j in range(n):
        if (i >> j) & 1:  # 真実を言ってる
            ans_temp += 1
            for x, y in xy[j]:
                if TF_lst[x - 1] == -1:
                    TF_lst[x - 1] = y
                elif TF_lst[x - 1] != y:
                    ok = False
                    break
    if ok:
        ans = max(ans, ans_temp)
print(ans)
