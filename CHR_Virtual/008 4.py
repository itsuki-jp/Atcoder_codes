# CHR_Virtual_08
s = input().split()
t = input().split()
check = [["R", "G", "B"], ["G", "B", "R"], ["B", "R", "G"]]
# 偶数手で完成できるかどうか
if (s in check) == (t in check):
    print("Yes")
else:
    print("No")
