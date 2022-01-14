n = int(input())
if n < 42:
    ans = "AGC"+"0" * (3 - len(str(n))) + str(n)
else:
    n = str(n + 1)
    ans = "AGC"+"0" * (3 - len(n)) + n
print(ans)
