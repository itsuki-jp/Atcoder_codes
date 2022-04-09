def make_divisors( n ):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


n = int(input())
lst = make_divisors(n)
ans = 0
for i in lst[1:]:
    cur = i - 1
    if n % cur == n // cur:
        ans += cur
print(ans)
