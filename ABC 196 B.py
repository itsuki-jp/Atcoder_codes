x = input()
if "." in x:
    num = x.index(".")
    print(x[:num])
else:
    print(x)