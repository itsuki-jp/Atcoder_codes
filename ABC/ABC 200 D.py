n = min(8, int(input()))
a = list(map(int, input().split()))
lst = [0] * 300


def output( num ):
    temp = str(bin(num))[2:]
    a = ""
    print(temp.count("1"), end=" ")
    for i in range(len(temp)):
        if temp[i] == "1":
            a = str(len(temp) - i) + " " + a
    print(a)


for i in range(1, 2 ** n):
    total = 0
    for j in range(n):
        if i >> j & 1:
            total += a[j]
    if lst[total % 200] == 0:
        lst[total % 200] = i
    else:
        print("Yes")
        output(lst[total % 200])
        output(i)
        exit()
print("No")
