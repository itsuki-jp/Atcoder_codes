# 解説
t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    if not 2 * l <= r:
        print(0)
        continue
    # 2 * l <= a <= r
    # 2 * l <= b + c <= r
    # l <= b <= r
    # l <= c <= r
    temp = r - l*2 + 1
    ans = (temp + 1) * temp // 2
    print(ans)

