n = int(input())
a = list(map(int, input().split()))
acc = 0
mx = 0
ans = 0
s = 0
for i in range(n):
    acc += a[i]
    mx = max(mx, acc)
    ans = max(ans, s + mx)
    s += acc
print(ans)
