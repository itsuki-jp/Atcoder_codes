#n = 回数　a　= 歩き　b = テレポート
n,a,b = map(int,input().split())
x = list(map(int,input().split()))
count = 0
for i in range(n-1):
    if a*(x[i+1] - x[i]) > b:
        count += b
    else:
        count += a*(x[i+1] - x[i])
print(count)