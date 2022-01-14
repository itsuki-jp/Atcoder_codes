x = int(input())
rate = [i for i in range(400,2000,200)]
rate.sort(reverse=True)
for i in range(8):
    if x >= rate[i]:
        print(i+1)
        exit()
