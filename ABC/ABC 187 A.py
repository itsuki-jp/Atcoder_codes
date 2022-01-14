a,b = input().split()
sum1 = 0
sum2 = 0
for i in a:
  sum1 += int(i)
for i in b:
  sum2 += int(i)
print(max(sum1,sum2))