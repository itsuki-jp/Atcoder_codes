a, b, n = map(int, input().split())
list1 = []
for cnt in range(n):
    test = int((a * cnt) / b) - (a * int((cnt / b)))
    list1.append(test)
print(max(list1))
