a, b, c = map(int, input().split())
if c > 0:
    a = a ** ((c % 2) + 2)
    b = b ** ((c % 2) + 2)
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")