n = int(input())
cnt = 0
lst = []
while cnt != 120:
    if n == 0:
        print(*lst[::-1],sep="")
        exit()
    if n % 2 == 1:
        n -= 1
        lst.append("A")
    else:
        n //= 2
        lst.append("B")
    cnt += 1

