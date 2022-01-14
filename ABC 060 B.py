a,b,c=map(int,input().split())
remain = [0]*1000
total = a
for i in range(100000):
    if total % b == c:
        exit(print("YES"))
    elif remain[total%b] >1:
        exit(print("NO"))
    else:
        remain[total%b] +=1
        total += a