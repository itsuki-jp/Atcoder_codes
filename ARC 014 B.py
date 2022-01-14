n = int(input())
list_w = [input() for counter in range(n)]
ans1 = 10
ans2 = 10


def rule_1():
    global ans1
    counter = 1
    list_rule1 = []
    for i in list_w:
        list_rule1.append(i)
        if len(list_w[:counter]) != len(set(list_rule1)):
            ans1 = counter
            rule_2()
        counter += 1
    rule_2()


def rule_2():
    global ans2
    for i in range(n - 1):
        a = list_w[i]
        b = list_w[i + 1]
        if a[-1] == b[0]:
            pass
        else:
            ans2 = i + 1
            last()
    ans2 = i + 2
    last()


def last():
    if ans1 == 10 and ans2 == 10:
        print("DRAW")
        exit()
    if min(ans1, ans2) % 2 == 0:
        print("WIN")
        exit()
    elif min(ans1, ans2) % 2 == 1:
        print("LOSE")
        exit()


rule_1()
