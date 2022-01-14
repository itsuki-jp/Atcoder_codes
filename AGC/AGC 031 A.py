from collections import Counter
n = int(input())
s = input()
c = list(Counter(s).most_common())
ans = 1
mod = 10 ** 9 + 7
for i in c:
    ans *= i[1] + 1
    ans %= mod
print(ans - 1)