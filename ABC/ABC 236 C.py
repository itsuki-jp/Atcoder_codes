n, m = map(int, input().split())
s = input().split()
t = input().split()
sets = set(t)
for i in s:
    if i in sets:
        print("Yes")
    else:
        print("No")
