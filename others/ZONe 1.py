alp = "abcdefghijklmnopqrstuvwxyz"
lst = "nopqrstuvwxyzabcdefghijklm"
while True:
    s = input()
    for i in s:
        n1 = alp.index(i)
        if n1 + 13 >= 26:
            print(alp[n1 + 13 - 26], end="")
        else:
            print(alp[n1 + 13], end="")
    print()
