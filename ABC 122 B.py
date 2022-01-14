s = input()
acgt = ["A","G","C","T"]
ans = 0
temp = 0
TF = True
for i in s:
    if i in acgt and TF:
        temp += 1
        ans = max(temp,ans)
    if i in acgt and not TF:
        temp = 1
        TF = True
    if i not in acgt:
        TF = False
        temp = 0
print(ans)