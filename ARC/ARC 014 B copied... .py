N = int(input())
W = [input() for _ in range(N)]
for i in range(1, N):
    if W[i][0] != W[i - 1][-1]:
        print('WIN') if (i % 2) else print('LOSE')
        exit(0)
    for j in range(i):
        if W[i] == W[j]:
            print('WIN') if (i % 2) else print('LOSE')
            exit(0)
print('DRAW')