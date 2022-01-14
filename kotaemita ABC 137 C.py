from collections import defaultdict
N = int(input())
dict = defaultdict(int)
ans = 0
for i in range(N):
    s = ''.join(sorted(input()))
    ans += dict[s]
    dict[s] += 1
print(ans)

"""n = int(input())
lst = []
num = [1]*n
ans = 0
s_all = [''.join(sorted(input())) for _ in range(n)]
for s in s_all:
    if s not in lst:
        lst.append(s)
    else:
        pos = lst.index(s)
        ans += num[pos]
        num[pos] += 1

print(int(ans))
"""