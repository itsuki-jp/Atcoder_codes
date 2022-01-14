n = int(input())
x = [0] * n
l = [0] * n
end_lst = [0] * n
start_lst = [0] * n
lst = []
for i in range(n):
    xt, lt = map(int, input().split())
    lst.append([xt + lt, xt - lt, i])
lst.sort()
pos = lst[0][0]
ans = 1
for i in range(1,n):
    if pos > lst[i][1]:
        continue
    ans += 1
    pos = lst[i][0]
print(ans)
