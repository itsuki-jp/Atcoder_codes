# aaba だと違う
s = list(input())
k = int(input())
l = len(s)
ans = 0
if len(set(s)) == 1:
    print(len(s) * k // 2)
elif s[0] != s[-1]:
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            s[i + 1] = "1"  # 前後の文字が同じだったら後の方文字を（他とかぶらない文字→適当な数字に）変更する
            ans += 1
    ans *= k  # k回繰り返すから、kかける
    print(ans)
else:
    a, b = 1, 1
    for i in range(l):
        if s[i] == s[i + 1]:
            a += 1
        else:
            break
    for i in range(l - 1, -1, -1):
        if s[i] == s[i - 1]:
            b += 1
        else:
            break
    cnt = 1
    for i in range(a, l - b):
        if s[i] == s[i + 1]:
            s[i + 1] = "1"  # 前後の文字が同じだったら後の方文字を（他とかぶらない文字→適当な数字に）変更する
            cnt += 1
        else:
            ans += cnt // 2
            cnt = 1
    ans *= k  # k回繰り返すから、kかける
    print(ans + a // 2 + b // 2 + (a + b) // 2 * (k - 1))
