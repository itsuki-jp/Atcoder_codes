a,b,c,d = map(int,input().split())

tak = b/a
aok = d/c
if tak > aok:
    print("TAKAHASHI")
elif tak < aok:
    print("AOKI")
else:
    print("DRAW")