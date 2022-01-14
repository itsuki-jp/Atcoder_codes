num = int(input())

def factorial_cor(n):
    fact = 1
    for integer in range(1, n + 1):
        fact *= integer
    return fact

print(factorial_cor(num) % ((10 ** 9) + 7))