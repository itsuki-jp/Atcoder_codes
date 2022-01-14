a, k = map(int, input().split())
money_want = 2 * (10 ** 12)
count_day = 0
if k == 0:
    print(money_want - a)
    quit()
while a < money_want:
    a += 1 + (a * k)
    count_day += 1
print(count_day)
