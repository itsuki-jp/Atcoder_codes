a,b,c,d = map(int,input().split())
taka_hp=a-d
aoki_hp=c-b
while True:
    if  aoki_hp <=0:
        print("Yes")
        exit()
    else:
        aoki_hp -= b
        if taka_hp <= 0:
            print("No")
            exit()
        else:
            taka_hp -= d