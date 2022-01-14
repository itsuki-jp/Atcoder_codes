import math


def permutations_count( n, r ):
    return math.factorial(n) // math.factorial(n - r)


def combinations_count( n, r ):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


print(combinations_count(4, 2))
