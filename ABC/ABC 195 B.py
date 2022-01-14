a,b,w = map(int,input().split())
nmin = float("inf")
nmax = 0
for i in range(1,1000001):
    if a * i <= w * 1000 <= b * i:
        nmin = min(nmin,i)
        nmax = max(nmax,i)
if nmax == 0:
    print("UNSATISFIABLE")
else:
    print(nmin,nmax)