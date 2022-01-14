a, b = map(int, input().split())
if a >= 12:
    a -= 12
a = (a*30 + b*0.5)
angle = a - b * 6

if 180 >= angle >= 0:
        print(angle)
elif angle > 180:
    print(angle - 180)
elif angle < 0:
    print(-1 * angle)
