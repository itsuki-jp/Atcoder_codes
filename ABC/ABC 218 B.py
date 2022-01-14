p = list(map(int, input().split()))
alp = "abcdefghijklmnopqrstuvwxyz"
for i in p:
    print(alp[i - 1],end="")