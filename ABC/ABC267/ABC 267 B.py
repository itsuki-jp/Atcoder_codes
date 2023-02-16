s = input()
if s[0] == "1":
    print("No")
    exit()
lst = [0] * 7
if s[0] == "1":
    lst[3] += 1
if s[1] == "1":
    lst[2] += 1
if s[2] == "1":
    lst[4] += 1
if s[3] == "1":
    lst[1] += 1
if s[4] == "1":
    lst[3] += 1
if s[5] == "1":
    lst[5] += 1
if s[6] == "1":
    lst[0] += 1
if s[7] == "1":
    lst[2] += 1
if s[8] == "1":
    lst[4] += 1
if s[9] == "1":
    lst[6] += 1
ans = "No"

for i in range(len(lst) - 1):
    if lst[i] != 0 and lst[i + 1] == 0 and sum(lst[i + 2:]) != 0:
        ans = "Yes"
lst = lst[::-1]
for i in range(len(lst) - 1):
    if lst[i] != 0 and lst[i + 1] == 0 and sum(lst[i + 2:]) != 0:
        ans = "Yes"
print(ans)
