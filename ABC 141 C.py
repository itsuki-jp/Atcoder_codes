n,k,q = map(int,input().split())
points = [int(input()) for _ in range(q)]
for i in range(q):
    winner = int(input())
    points[winner - 1] += 1
for i in points:
    if i >0:
        print("Yes")
    else:
        print("No")