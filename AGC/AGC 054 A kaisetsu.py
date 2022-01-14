# 解説
n = int(input())
s = list(input())
if s[0] != s[-1]:
    print(1)
else:
    for i in range(1, n - 1):
        if s[0] != s[i] and s[-1] != s[i + 1]:
            print(2)
            break
    else:
        print(-1)
