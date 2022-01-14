n = int(input())
list1 = []
for i in range(n):
    s, p = input().split()
    p = int(p)
    list1.append((s, -p, i + 1))
list1.sort()
for i in range(n):
    print(list1[i][2])


