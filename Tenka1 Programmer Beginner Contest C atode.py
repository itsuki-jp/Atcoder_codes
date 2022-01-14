import itertools

a = [1,2, 3, 4, 5, 9,10]
n = len(a)
p = itertools.permutations(a)
ans = 0
lst = []
for i in p:
    temp = 0
    for j in range(5):
        temp += abs(i[j] - i[j + 1])
    if temp > ans:
        lst = i
        ans = temp
print(lst)

ans_lst1 = [0] * (n + 10)
ans_lst2 = [0] * (n + 10)
for i in range(n):
    if i % 2 == 0:
        ans_lst1.append()

