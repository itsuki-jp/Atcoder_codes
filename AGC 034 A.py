n,a,b,c,d = [int(x) - 1 for x in input().split()]
s = input()
n += 1
if c < d:
    if "##" in s[a:d+1]:
        print("No")
    else:
        print("Yes")

else:
    if "##" not in s[a:c+1] and "..." in s[b-1:d+2]:
        print("Yes")
    else:
        print("No")
