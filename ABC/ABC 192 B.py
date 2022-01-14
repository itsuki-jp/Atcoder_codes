s = input()
s1 = s[::2]
s2 = s[1::2]
if s1 == s1.lower() and s2 == s2.upper():
    print("Yes")
else:
    print("No")