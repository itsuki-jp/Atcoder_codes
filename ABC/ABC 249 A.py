a, b, c, d, e, f, x = map(int, input().split())
tak = (a + c) // x * b + min(a, (a + c) % x) * b
aok = (d + f) // x * e + min(d, (d + f) % x) * e
if tak > aok:
    print("Takahashi")
elif tak < aok:
    print("Aoki")
else:
    print("Draw")
