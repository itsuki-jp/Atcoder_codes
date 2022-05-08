n = int(input())
A = [int(input()) for _ in range(n)]
for a in A:
    if a % 2 != 0:
        print("first")
        exit()
print("second")
