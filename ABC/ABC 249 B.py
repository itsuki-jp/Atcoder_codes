lw = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
      'x', 'y', 'z']
up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
      'X', 'Y', 'Z']
s = input()
tf = [False, False]
for i in lw:
    if s.count(i) < 1:
        continue
    elif s.count(i) == 1:
        tf[0] = True
    else:
        exit(print("No"))
for i in up:
    if s.count(i) < 1:
        continue
    elif s.count(i) == 1:
        tf[1] = True
    else:
        exit(print("No"))
if tf[0] == tf[1] == True:
    print("Yes")
else:
    print("No")
