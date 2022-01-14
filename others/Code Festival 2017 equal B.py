n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int,input().split()))
p = {}
for j in d:
    if j not in p:
        p[j] = 1
    else:
        p[j] += 1
for i in t:
    if i not in p or p[i] == 0:
        print("NO")
        exit()
    p[i] -= 1
print("YES")