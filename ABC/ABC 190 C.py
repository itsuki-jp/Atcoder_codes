n,m = map(int,input().split())
lst_ab = []
for _ in range(m):
    ab = list(map(int,input().split()))
    lst_ab.append(ab)
k = int(input())
lst_cd = []
for _ in range(k):
    cd = list(map(int, input().split()))
    lst_cd.append(cd)
for i in range(2**k):
