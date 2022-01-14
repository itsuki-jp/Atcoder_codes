n = input()
for i in range(14):
    if n == n[::-1]:
        print("Yes")
        exit()
    else:
        n = "0"+n
print("No")