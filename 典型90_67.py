n,k = input().split()
if n == "0":
    print(0)
    exit()
k = int(k)
for _ in range(k):
    n = str(n)
    num = 0
    # 8進法から10進法に変換する
    j = 1
    for i in range(len(n)):
         num += int(n[-i - 1]) * j
         j *= 8
    # 10進法から9進法に変換する
    j = 1
    temp = ""
    while num != 0:
        temp += str(num % 9)
        num //= 9
    n = int(temp.replace("8","5")[::-1])
print(n)
