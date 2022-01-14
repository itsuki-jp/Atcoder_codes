#シカのAtCoDeerくんは二つの正整数 a,b を見つけました。 a と b の積が偶数か奇数か判定してください
a, b = map(int,input().split())

a_check=a%2
b_check=b%2
if a_check == int(0):
    print("Even")
else:
    if b_check == int(0):
        print("Even")
    else:
        print("Odd")