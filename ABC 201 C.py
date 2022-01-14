# 下に大作あり
s = list(input())
ans = 0
for i in range(10**4):
    p = str(i)
    while len(p) < 4:
        p = "0" + p
    TF = True
    for j in range(10):
        if not TF:
            break
        if s[j] == "o" and str(j) in p:
            continue
        if s[j] == "?":
            continue
        if s[j] == "x" and str(j) not in p:
            continue
        TF = False
    if TF:
        ans += 1
print(ans)

"""
超大作
s = input()
o = []
q = []
for i in range(10):
    if s[i] == "o":
        o.append(str(i))
    elif s[i] == "?":
        q.append(str(i))
if len(o) > 4 or len(o) + len(q) == 0:
    print(0)
    exit()
ans = 0
for i in range(10):
    if str(i) not in o and str(i) not in q:
        continue
    for j in range(10):
        if str(j) not in o and str(j) not in q:
            continue
        for k in range(10):
            if str(k) not in o and str(k) not in q:
                continue
            for l in range(10):
                if str(l) not in o and str(l) not in q:
                    continue
                co = 0
                co2 = 0
                co2_lst = []
                cq = 0
                if str(i) in o:
                    co += 1
                    if i not in co2_lst:
                        co2_lst.append(i)
                        co2 += 1
                elif str(i) in q:
                    cq += 1
                if str(j) in o:
                    co += 1
                    if j not in co2_lst:
                        co2_lst.append(j)
                        co2 += 1
                elif str(j) in q:
                    cq += 1
                if str(k) in o:
                    co += 1
                    if k not in co2_lst:
                        co2_lst.append(k)
                        co2 += 1
                elif str(k) in q:
                    cq += 1
                if str(l) in o:
                    co += 1
                    if l not in co2_lst:
                        co2_lst.append(l)
                        co2 += 1
                elif str(l) in q:
                    cq += 1
                temp = str(i) + str(j) + str(k) + str(l)
                if co2 == len(o) and co + cq <= 4:
                    ans += 1
print(ans)
"""

