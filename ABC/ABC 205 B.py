n = int(input())
a = sorted(list(map(int,input().split())))
if list(range(1,n+1)) == a:
    print("Yes")
else:
    print("No")