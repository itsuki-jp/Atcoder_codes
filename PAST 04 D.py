n = int(input())
s = input()
lst = list(s.split("#"))
num = 0
for i in lst:
    if len(i) > num:
        num = len(i)
num2 = s.index("#")
num3 = s[::-1].index("#")

if num == 0:
    print(0, 0)
elif num <= num2 + num3:
    print(num2, num3)
else:
    print(num-num3, num3)
