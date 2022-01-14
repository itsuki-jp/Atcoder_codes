a,b,c = map(int,input().split())
if c - b == b - a or b - c == c - a or a - c == c - b or c - a == a - b or a - b == b - a or b - a == a - c:
    print("Yes")
else:
    print("No")
