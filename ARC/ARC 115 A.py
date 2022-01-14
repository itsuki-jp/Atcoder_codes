n,m = map(int,input().split())
odd = 0
even = 0
for _ in range(n):
    s = input().count("1")
    if s % 2 == 0:
        even += 1
    else:
        odd += 1
print(odd * even)