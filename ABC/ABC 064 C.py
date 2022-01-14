n = int(input())
a = list(map(int,input().split()))
rate = [False]*8
over = 0
for i in a:
    for j in range(1,9):
        if i < j*400:
            rate[j-1] = True
            break
        if j == 8 and i >= 3200:
            over += 1
if over:
    print(sum(rate),min(8,sum(rate)+over))
else:
    if sum(rate):
        print(sum(rate),sum(rate))
    else:
        print(1,sum(rate))