from collections import Counter
l = list(map(int, input().split()))
count = list(Counter(l).values())
if len(count) == 2 and 2 in count and 3 in count:
    print("Yes")
else:
    print("No")