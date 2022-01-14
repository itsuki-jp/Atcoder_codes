s = list(input())
sets= len(set(s))
if sets == 1:
    print(1)
elif sets == 2:
    print(3)
else:
    print(6)