n, m = map(int, input().split())
ac_list = [0]*n
wa_list = [0]*n
AC = 0
WA = 0
for _ in range(m):
    p, s = input().split()
    p = int(p) - 1
    if ac_list[p] == 0:
        if s == "WA":
            wa_list[p] += 1
        else:
            ac_list[p] = 1
            AC += ac_list[p]
            WA += wa_list[p]


print(AC, WA)
