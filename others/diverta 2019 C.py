n = int(input())
ans = 0
a = 0  # 最後がA
b = 0  # 最初がB
both = 0  # Bで始まり、Aで終わる
for _ in range(n):
    s = input()
    ans += s.count("AB")
    if s[-1] == "A" and s[0] == "B":
        both += 1
    elif s[-1] == "A":
        a += 1
    elif s[0] == "B":
        b += 1

sml = min(a, b)
if both == 0:
    ans += sml
else:
    if a + b > 0:
        ans += both + sml
    else:
        ans += both - 1
print(ans)
