from itertools import permutations
from collections import Counter

s = list(input())
c = Counter(s)
if len(s) == 1:
    if int(s[0]) % 8 == 0:
        exit(print("Yes"))
if len(s) == 2:
    if 10 * int(s[0]) + int(s[1]) % 8 == 0 or 10 * int(s[1]) + int(s[0]) % 8 == 0:
        exit(print("Yes"))
for _ in permutations(range(1, 10), 3):
    _ = [str(_) for _ in _]
    temp = int("".join(_))
    if int(temp) % 8 == 0:
        c_temp = Counter(_)
        for i in range(1, 10):
            if c_temp[str(i)] > c[str(i)]:
                break
        else:
            exit(print("Yes"))
print("No")
