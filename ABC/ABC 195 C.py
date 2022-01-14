l = input()
n = int(l)
l = len(l)

if 3 >= l:
    print(0)
elif 6 >= l:
    print(n-999)
elif 9 >= l:
    print(n - 999999 + (n - 999))
elif 12 >= l:
    print(n - 999999999 + (n - 999999 + n - 999))
elif 15 >= l:
    print(n - 999999999999 + (n - 999999999 + n - 999999 + n - 999))
else:
    print(n - 999999999999999 + (n - 999999999999 + (n - 999999999 + n - 999999 + n - 999)))