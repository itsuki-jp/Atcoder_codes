a = set(list(input().split()))
b = set(list(input().split()))
clutch = [0, 0]
ace = [set(), set()]
while len(a) != 0 and len(b) != 0:
    x, y = input().split()
    if x in a:
        ace[0].add(x)
        if len(a) == 1 and len(b) >= 2:
            clutch[0] = x
        b.remove(y)
    else:
        ace[1].add(x)
        if len(b) == 1 and len(a) >= 2:
            clutch[1] = x
        a.remove(y)
win = 0
if len(a) == 0:
    win = 1
print("AB"[win])
print(f"clutch:{clutch[win] if clutch[win] != 0 else ''}")
print(f"ace:{ace[win].pop() if len(ace[win]) == 1 else''}")
