n,m = map(int,input().split())
ans = [0 for _ in range(m)]
num = 0
for i in range(n):
  a = list(map(int,input().split()))
  for j in a[1::]:
    ans[j-1] += 1
for i in ans:
  if i == n:
    num += 1
print(num)