n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
fav = max(a)
for bi in b:
    if a[bi - 1] == fav:
        exit(print("Yes"))
print("No")
