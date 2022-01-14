n = int(input())
s = list(input())
if "#" not in s or "." not in s:
    exit(print(0))  # 元々白か黒しかなかったら、変更する場所はない

W = s.count(".")
B = 0
ans = W
for i in range(n):
    temp = 0
    if s[i] == "#":
        B += 1
    else:
        W -= 1
    temp = B + W
    ans = min(ans,temp)
print(ans)
