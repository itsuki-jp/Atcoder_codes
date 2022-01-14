import random

ans = []
num = [i for i in range(1, 10)]
for i in range(4):
    num_remove = random.randint(0, 8 - i)
    ans.append(num.pop(num_remove))
print(ans)


def check( user_input ):
    if user_input == ans:
        return True
    else:
        hit = 0
        blow = 0
        for i in range(4):
            if user_input[i] == ans[i]:
                hit += 1
            if user_input[i] in ans:
                blow += 1
        print(f"hit : {hit}, blow : {blow - hit}")
        return False


trial = 1
TF = True
while TF:
    user = list(map(int,input("Enter 4 digits number : ").split()))
    if len(user) != 4:
        print("----------------------------")
        continue
    if check(user):
        print("You got it!")
        print(f"Number of trial is {trial}")
        TF = False
    else:
        print("----------------------------")
        trial += 1
