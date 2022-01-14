sx,sy,tx,ty = map(int,input().split())

x1 = tx-sx
y1 = ty-sy
print("U"*y1+"R"*x1+"D"*y1+"L"*x1+"L"+"U"*(1+y1)+"R"*(1+x1)+"D"+"R"+"D"*(1+y1)+"L"*(1+x1)+"U")




