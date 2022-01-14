sx,sy,gx,gy = map(int,input().split())
ans = (gx-sx) / (gy/sy + 1)
print(ans + sx)