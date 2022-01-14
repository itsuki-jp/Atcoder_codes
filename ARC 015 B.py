mousho = 0
manatsu = 0
natsu = 0
nettai = 0
huyu = 0
mahuyu = 0
"""
猛暑日：MAX 35度以上の日
真夏日：MAX 30度以上、35度未満の日
夏日　：MAX 25度以上、30度未満の日
熱帯夜：最低気温が 25度以上の日
冬日　：最低気温が 0度未満で、MAX 0度以上の日
真冬日：MAX 0度未満の日
"""

n = int(input())
for i in range(n):
    t_max, t_min = map(float, input().split())
    if t_max >= 35:
        mousho += 1
    if 30 <= t_max < 35:
        manatsu += 1
    if 25 <= t_max < 30:
        natsu += 1
    if t_min >= 25:
        nettai += 1
    if t_min < 0 <= t_max:
        huyu += 1
    if t_max < 0:
        mahuyu += 1
print(mousho, manatsu, natsu, nettai, huyu, mahuyu)
