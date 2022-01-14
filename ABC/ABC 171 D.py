n = int(input())
a = list(map(int,input().split()))
q = int(input())
ans = sum(a)
a_list = [0]*(10**5)
for i in a:
    a_list[i-1] += 1

for j in range(q):
    b,c = map(int,input().split())
    a_list[c-1] += a_list[b - 1]
    ans += (c - b) * a_list[b -1]
    a_list[b-1]=0
    print(ans)