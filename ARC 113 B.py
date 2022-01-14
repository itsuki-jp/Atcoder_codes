A, B, C = map(int, input().split())
if B == 1:
    print(A % 10)
    exit()
if B < 10 and C < 10 and B ** C < 10:
    print(pow(A, pow(B, C), 10))
    exit()
rem = [pow(A, d, 10) for d in range(11)]
for i in range(10):
    if rem[i] in rem[:i]:
        j = rem.index(rem[i])
        d = i - j
        print(rem[j + (pow(B, C, d) - j) % d])
        exit()