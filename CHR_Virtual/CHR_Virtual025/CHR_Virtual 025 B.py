n = int(input())
lst = []
for _ in range(n):
    temp = input().split()
    lst.append((int(temp[1]), temp[0]))
lst.sort()
print(lst[-2][1])
