n,k = map(int,input().split())
p = sorted(list(map(int,input().split())),reverse=True)
kitai = [0]*p[0]
ans = 0

for i in range(k):
  num = p[i]
  if kitai[num-1] == 0:
    temp = 0
    for j in range(1,num+1):
      temp += (j * (1/num))
    kitai[num-1] = temp
    ans += temp
  else:
    ans += kitai[num-1]
print(ans)