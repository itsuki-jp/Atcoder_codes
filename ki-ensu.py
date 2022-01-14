s = input()
ans = "keyence"
if ans in s:
    print("YES")
    exit()
for i in range(8):
    if ans[:i+1] ==s[:i+1]:
        if ans[8-i:] == s[len(s)-i:]:
            print("YES")
            exit()
print("NO")
