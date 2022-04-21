n = int(input())
a = set(list(map(int, input().split())))
for i in range(3000):
    if i not in a:
        print(i)
        break
