n = int(input())
a = []
b = []

for i in range(n):
    a_temp, b_temp = map(int, input().split())
    a.append(a_temp)
    b.append(b_temp)

ans = 0
a = a[::-1]
b = b[::-1]
for i in range(n):
    ans += (-(a[i] + ans)) % b[i]
print(ans)
