import copy

s = input()
lst = []
for i in s:
    lst.append(int(i))

if len(s) == 1:
    if int(s) % 8 == 0:
        print("Yes")
        exit()
    else:
        print("No")
        exit()
if len(s) == 2:
    if int(s) % 8 == 0:
        print("Yes")
        exit()
    elif (int(s[1]) * 10 + int(s[0])) % 8 == 0:
        print("Yes")
        exit()
    else:
        print("No")
        exit()

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if (100 * i + 10 * j + k) % 8 == 0:
                lst2 = copy.copy(lst)
                if i in lst2:
                    lst2.remove(i)
                    if k in lst2:
                        lst2.remove(k)
                        if j in lst2:
                            print("Yes")
                            exit()
print("No")
