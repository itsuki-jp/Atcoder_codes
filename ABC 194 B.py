n = int(input())
a_lst = []
b_lst = []
temp = float("inf")
ans = float("inf")
for i in range(n):
    a, b = map(int, input().split())
    a_lst.append(a)
    b_lst.append(b)
    temp = min(temp, a + b)
mina = min(a_lst)
minb = min(b_lst)
ans = max(mina, minb)
print(min(temp, ans))
