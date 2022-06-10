n = int(input())
length = len(str(n))
past = 0
for i in range(length):
    if i != (length - 1):
        temp = 10 ** (i + 1) - 10 ** i
        past += (1 + temp) * temp // 2
    else:
        temp = n - 10 ** i + 1
        ans = past + (1 + temp) * temp // 2
        print(int(ans) % 998244353)
