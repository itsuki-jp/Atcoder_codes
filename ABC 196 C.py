n = input()
len_n = len(n) // 2
n = int(n)
ans = 0
for i in range(1,1 + 10 **  len_n):
    num = str(i) + str(i)
    if n >= int(num):
        ans += 1
print(ans)
