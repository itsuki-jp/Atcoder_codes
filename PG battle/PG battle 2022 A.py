n = int(input())
b = list(map(int, input().split()))
b.sort()
diff = (b[-1] - b[0]) // n
sets = set(b)
for i in range(n):
    if (b[0] + diff * i) not in sets:
        print(b[0] + diff * i)
