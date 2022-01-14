s = input()
q = int(input())

for counter in range(q):
    number = input().split()
    if len(number) ==1:
        s[::-1]
    else:
        if number[1] == 1:
            s += number[2]
        else:
            s = number[2] + s

print(s)
