import math


def combinations_count( n, r ):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


a, b, k = map(int, input().split())
ans = ""
for i in range(a + b):
    if k == 0:
        ans = ans + "a" * a + "b" * b
        print(ans)
        exit()
    if b == 0:
        ans = ans + "a" * a
        print(ans)
        exit()
    if a == 0:
        ans = ans + "b" * b
        print(ans)
        exit()
    temp = combinations_count(a+1, b)
    if k > temp:
        ans = ans + "b"
        b -= 1
    else:
        ans = ans + "a"
        a -= 1
    k -= temp
print(ans)
