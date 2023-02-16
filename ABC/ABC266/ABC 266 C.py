import math
import numpy as np


def degree( x0, y0, x1, y1, x2, y2 ):
    vec1 = [x1 - x0, y1 - y0]
    vec2 = [x2 - x0, y2 - y0]
    absvec1 = np.linalg.norm(vec1)
    absvec2 = np.linalg.norm(vec2)
    inner = np.inner(vec1, vec2)
    cos_theta = inner / (absvec1 * absvec2)
    theta = math.degrees(math.acos(cos_theta))
    return theta


lst = [list(map(int, input().split())) for _ in range(4)]
lst = lst * 4
ans = 0
for i in range(4):
    ang = degree(lst[i + 1][0], lst[i + 1][1], lst[i][0], lst[i][1], lst[i + 2][0], lst[i + 2][1])
    ans += ang
eps = 10 ** -5
if 360 - eps <= ans <= 360 + eps:
    print("Yes")
else:
    print("No")
