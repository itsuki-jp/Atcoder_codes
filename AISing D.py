n = int(input())
x = input()


def sousa(num, ans):
    num_b = format(num, 'b')
    cnt_s = num_b.count("1")
    num %= cnt_s
    if num == 0:
        print(ans)
    else:
        sousa(num, ans + 1)


for i in range(n):
    temp = list(x)
    if temp[i] == "1":
        temp[i] = "0"
    else:
        temp[i] = "1"
    temp = int("".join(temp), 2)
    sousa(temp, 1)
