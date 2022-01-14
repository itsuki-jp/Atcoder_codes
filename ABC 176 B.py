n = input()
cnt = 0
for i in n:
    i = int(i)
    cnt += i
if cnt % 9 == 0:
    print("Yes")
else:
    print("No")