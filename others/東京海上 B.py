a,v = map(int,input().split())
b,w = map(int,input().split())
t = int(input())
if b > a:
    av = a + v * t
    bw = b + w * t

    if av >= bw:
        print("YES")
    else:
        print("NO")
else:
    av = a - v * t
    bw = b - w * t
    

    if av <= bw:
        print("YES")
    else:
        print("NO")