n = int(input())
ans = 0
a_last = 0
b_head = 0
both = 0
for _ in range(n):
    s = input()
    ans += s.count("AB")
    if s[-1] == "A" and s[0] == "B":
        both += 1
    elif s[-1] == "A":
        a_last += 1
    elif s[0] == "B":
        b_head += 1

ans += min(a_last, b_head)
remain = abs(a_last - b_head)
if both > 0:

ans += both + remain - 1 if both > 0 else 0
print(ans)
