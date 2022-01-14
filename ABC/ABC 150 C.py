import itertools
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
num = [i for i in range(1,n+1)]
lst = list(itertools.permutations(num))
pos_p = 0
pos_q = 0
for i in range(len(lst)):
    temp = list(lst[i])
    if temp == p:
        pos_p = i
    if temp == q:
        pos_q = i
print(abs(pos_p - pos_q))

