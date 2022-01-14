n,w = map(int,input().split())
litre = [0 for _ in range(210000+1)]
for _ in range(n):
    s, t, p = list((map(int, input().split())))
    litre[s] += p
    litre[t] -= p


for i in range(210000):
    litre[i+1] += litre[i]
    if litre[i] > w:
        exit(print("No"))
print("Yes")