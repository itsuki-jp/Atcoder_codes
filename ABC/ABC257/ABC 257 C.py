from bisect import *

n = int(input())
s = input()
w = list(map(int, input().split()))
child = [w[_] for _ in range(n) if s[_] == "0"]
adult = [w[_] for _ in range(n) if s[_] == "1"]
child.sort()
adult.sort()
w.append(0)
w.append(10 ** 10)
all_weight = list(set(w))
all_weight.sort()
ans = 0
for weight in all_weight:
    temp = bisect_left(child, weight) + (len(adult) - bisect_left(adult, weight))
    n1 = bisect_left(child, weight)
    n2 = (len(adult) - bisect_left(adult, weight))
    ans = max(ans, temp)
print(ans)
