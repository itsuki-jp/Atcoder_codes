n = int(input())
a = list(map(int, input().split()))
lst = [4 for _ in range(n)]
for i in a:
    lst[i - 1] -= 1

print(lst.index(1) + 1)
