import collections
n = int(input())
a = [int(input()) for _ in range(n)]
b = [i for i in range(1,n+1)]
s = collections.Counter(a)
c = s.most_common()
common = c[0][0]
a = list(set(a))
for j in a:
    if j in b:
        b.remove(j)
if len(b) ==0:
    print("Correct")
else:
    print(common,*b)
