h, w, n = map(int, input().split())
a = []
b = []
for i in range(n):
    at,bt = map(int, input().split())
    a.append(at)
    b.append(bt)

a_dict = {v: i + 1 for i, v in enumerate(sorted(set(a)))}
b_dict = {v: i + 1 for i, v in enumerate(sorted(set(b)))}

for i,j in zip(a,b):
    print(a_dict[i],b_dict[j])
