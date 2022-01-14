n = input()
num = len(n) - 1
if n[num] ==str(2) or n[num] ==str(4) or n[num] == str(5) or n[num] == str(7) or n[num] == str(9):
    print("hon")
elif n[num] ==str(0) or n[num] ==str(1) or n[num] ==str(6) or n[num] ==str(8):
    print("pon")
else:
    print("bon")