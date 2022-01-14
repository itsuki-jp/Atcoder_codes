a = int(input())
ans = 0
for i in range(a):
  for j in range(a):
    if i > 0 and j > 0 and i + j == a:
      ans += 1
print(ans)