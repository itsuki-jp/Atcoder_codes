n = int(input())
a = list(map(int, input().split()))
cnt = 0
while all(i%2==0 for i in a):   #組み込み関数
    a = [i/2 for i in a]
    cnt += 1
print(cnt)
"""
a_original = input()
a_list0 = a_original.split()
a_list = [int(s) for s in a_list0]
for counter in range(9):
    count = counter
    for i in range(n):
        even_odd = a_list[i] % 2
        if even_odd == int(0):
            new_num = (a_list[i]) / 2
            a_list.insert(i, new_num)
            del a_list[i + 1]
        else:
            break
    else:
        continue
    break
"""

print(count)
