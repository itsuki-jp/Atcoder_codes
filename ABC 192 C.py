n,k = input().split()
n = [int(i) for i in n]
k = int(k)

for i in range(k):
    g1 = sorted(n,reverse=True)
    g2 = sorted(n)
    g1num = sum([g1[i]*10**(len(g1)-i-1) for i in range(len(g1))])
    g2num = sum([g2[i]*10**(len(g2)-i-1) for i in range(len(g2))])
    n = g1num - g2num
    n = [int(i) for i in str(n)]
print(sum([n[i]*10**(len(n)-i-1) for i in range(len(n))]))