n = int(input())
a = list(map(int, input().split()))
mod = 1000000007
rgb = [0, 0, 0]
ans = 1
for i in a:
    if i in rgb:
        cnt = rgb.count(i)
        ans *= cnt
        rgb[rgb.index(i)] = i + 1
        ans %= mod
    else:
        ans = 0
        break
print(ans)
