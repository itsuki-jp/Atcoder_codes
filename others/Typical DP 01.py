n = int(input())
p = list(map(int, input().split()))
total = sum(p)
lst = [0] * (total + 1)
lst[0] = 1
for i in p:
    for j in range(total, -1, -1):
        if lst[j] == 1:
            lst[i + j] = 1
print(lst.count(1))
