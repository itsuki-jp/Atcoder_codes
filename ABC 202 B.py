s = list(input())[::-1]
for i in s:
    if i == "6":
        print(9,end = "")
    elif i == "9":
        print(6,end = "")
    else:
        print(i,end = "")
