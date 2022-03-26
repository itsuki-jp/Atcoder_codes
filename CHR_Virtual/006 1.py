n = int(input())
r = [int(_) for _ in input().split()]
c = [int(_) for _ in input().split()]
q = int(input())
ans = []
for _ in range(q):
    rt, ct = [int(_) - 1 for _ in input().split()]
    if r[rt] + c[ct] <= n:
        ans.append(".")
    else:
        ans.append("#")
print(*ans, sep="")
