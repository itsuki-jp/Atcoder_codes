from itertools import product

n = int(input())
for s in product(["(", ")"], repeat=n):
    score = 0
    res = ""
    for i in range(n):
        if s[i] == "(":
            score += 1
        else:
            score -= 1
        res += s[i]
        if score < 0:
            break
    else:
        if score == 0:
            print(res)
