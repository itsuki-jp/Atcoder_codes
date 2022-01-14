def f( x ):
    if x == 1:
        return "ok"
    if x % 2 == 0:
        return f(x // 2)
    else:
        return f(x * 3 + 1)


def fib( x ):
    if x == 1:
        return 1
    if x == 2:
        return 1
    return fib(x - 1) + fib(x - 2)


for _ in range(1, 10):
    print(fib(_))
