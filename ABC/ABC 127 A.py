one_1 = []
one_2 = []
one_3 = []
for i in range(1,1000):
    I = str(i) + "000"
    if I[0] == "1":
        print(i)
        if I[1] == "1" and I[2] == "1":
            one_3.append(i)
        elif I[1] == "1":
            one_2.append(i)
        else:
            one_1.append(i)
print(one_1)
print(one_2)
print(one_3)
