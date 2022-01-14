n = int(input())
a = list(map(int, input().split()))

money = 1000

for i in a:
    low = i
    for j in a[i+1::]:
        if i < j:
            break