n = int(input())
s = input()
for i in range(n):
    if s[i] == str(1):
        if i % 2 == 0:
            print("Takahashi")
            break
        else:
            print("Aoki")
            break

