n = int(input())
s = input()

if n % 2 == 0:
    n //= 2
else:
    print("No")
    exit()
s2 = s[n:]
for i in range(n):
    if s[i] != s2[i]:
        print("No")
        exit()
print("Yes")