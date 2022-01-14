h,w = map(int,input().split())
if h == 1 or w == 1:
    print(h * w)
    exit()
if h % 2 == 0:
    h //= 2
else:
    h = h//2 + 1
if w % 2 == 0:
    w //= 2
else:
    w = w // 2 + 1
print(h * w)