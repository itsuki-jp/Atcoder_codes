n,m = map(int,input().split())
num_c = (4*n - m)/2
if num_c == int(num_c) and 0 <= num_c <= n:
    print("Yes")
else:
    print("No")
