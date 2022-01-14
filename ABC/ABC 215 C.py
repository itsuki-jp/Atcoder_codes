import itertools
s,k = input().split()
k = int(k)
s = list(s)
lst = list(set(list(itertools.permutations(s,len(s)))))
lst.sort()
print(*list(lst[k - 1]),sep="")
