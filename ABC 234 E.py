x = int(input())
lst = []
for i in range(10):  # 一番下の桁の数字
    for step in range(-9, 10):  # step
        temp = i
        TF = True
        while temp < x:
            s = str(temp)
            temp = int(str(int(s[0]) + step) + s)
            if temp < 0 or int(str(int(s[0]) + step)) == 0 or len(str(int(s[0]) + step)) > 1:
                TF = False
                break
        if TF:
            lst.append(temp)
print(sorted(lst)[0])
