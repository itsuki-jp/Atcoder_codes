s = int(input())
multi_2019 = [str(2019 * a) for a in range(s//2019 +1)]
ans = 0
s=str(s)
for i in multi_2019:
    if i in s:
       ans += 1
print(ans)