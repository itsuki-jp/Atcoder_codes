n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_set = set(a)
b_set = set(b)
ans1, ans2 = 0, 0
for i in range(n):
    if a[i] == b[i]:
        ans1 += 1
    elif a[i] in b_set:
        ans2 += 1
print(ans1)
print(ans2)
