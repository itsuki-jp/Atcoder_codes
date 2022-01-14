c = int(input())
n,m,l = 0,0,0
for i in range(c):
    nml = sorted(list(map(int,input().split())))
    n,m,l = max(nml[0],n),max(nml[1],m),max(nml[2],l)
print(n*m*l)
