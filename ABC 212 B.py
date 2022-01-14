x = input()
num = "01234567890123456789012345678901234567890"
if x in num or len(set(list(x))) == 1:
    print("Weak")
else:
    print("Strong")
