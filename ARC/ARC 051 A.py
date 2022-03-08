def dist( x, y ):
    return (x - x1) ** 2 + (y - y1) ** 2 <= r ** 2


x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())
red = "YES"
blue = "YES"
if x2 <= x1 - r and x1 + r <= x3 and y2 <= y1 - r and y1 + r <= y3:
    red = "NO"
elif dist(x2, y2) and dist(x3, y2) and dist(x2, y3) and dist(x3, y3):
    blue = "NO"
print(red)
print(blue)
