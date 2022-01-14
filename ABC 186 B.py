h,w = map(int, input().split())
a_lst = []
num = 9999999999
for i in range(h):
    a = list(map(int, input().split()))
    num = min(num,min(a))
    a_lst.append(a)
ans = 0
for i in a_lst:
    for j in i:
       ans += (j - num)
print(ans)