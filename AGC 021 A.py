n = int(input())
num = list(str(n))
ans = sum([int(i) for i in num])
temp = int(num[0]) - 1 + (len(num) - 1) * 9
print(max(ans, temp))
