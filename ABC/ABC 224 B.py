# -*- coding: utf-8 -*-
h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
for i1 in range(h - 1):
    for i2 in range(i1 + 1, h):
        for j1 in range(w - 1):
            for j2 in range(j1 + 1, w):
                if not a[i1][j1] + a[i2][j2] <= a[i2][j1] + a[i1][j2]:
                    exit(print("No"))
print("Yes")