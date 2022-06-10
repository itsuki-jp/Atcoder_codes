w = int(input())
lst = []
for i in range(1, 100):
    lst.append(i)
    lst.append(i * 100)
    lst.append(i * 10 ** 4)
print(len(lst))
print(*lst)
