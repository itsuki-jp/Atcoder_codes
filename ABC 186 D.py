import itertools
n = int(input())
a = list(map(int, input().split()))
lst = list(itertools.combinations(a,2))
ans = 0
for i in lst:
    ans += abs(i[0] - i[1])
print(ans)