a,b,c = map(int,input().split())
#a,b,cの中に偶数があれば0, 無かったら最大の数を半分にした数
if a%2 == 0 or b%2 == 0 or b%2 == 0:
    print(0)
    exit()

max_num = max(a,b,c)
num = max_num//2
num2 = max_num - num

if max_num == a:
    print((num2- num)*b*c)
    exit()
if max_num == b:
    print((num2 - num)*a*c)
    exit()
if max_num == c:
    print((num2 - num)*a*b)
    exit()