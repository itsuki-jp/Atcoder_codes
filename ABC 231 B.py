from collections import Counter
n = int(input())
lst = [input() for _ in range(n)]
a = Counter(lst)
a,b = zip(*a.most_common())
print(a[0])
