n,m=map(int,input().split())
s=list(map(int,input().split()))
s.sort(reverse=True)
total_vote=0
for i in range(n):
    total_vote += s[i]

count = 0
while count != m:
    if total_vote * (1/(4*m)) > s[count]:
        print("No")
        exit()
    else:
        count+=1
print("Yes")