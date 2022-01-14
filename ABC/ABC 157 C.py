# sとcの二次元リスト作って、sでソートする
# [[1,2][1,3][2,1][2,3]]的な
# で、最初の数（上のやつだと1番目と3番目）をans_listに入れる
"""
n, m = map(int, input().split())
ans_list = ["0"] * n
list1 = []
for i in range(m):
    s, c = map(int, input().split())
    a = [s, c]
    list1.append(a)
list1.sort()
for j in range(m):
counter_int = 1
counter_str = str()
for i in range(m):
    counter_str = str(counter_int)
    if list1[i][0] == counter_str:
        ans_list[counter_int -1] = list1[i][1]
        counter_int += 1
print(ans_list)
"""

n, m = map(int, input().split())
ans_list = [0] * n
list1 = []
for i in range(m):
    s, c = map(int, input().split())
    a = [s, c]
    list1.append(a)
list1.sort(reverse=True)
for i in range(m):
    s = list1[i][0]
    c = list1[i][1]
    if c == 0:
        ans_list[s - 1] = 0
    elif ans_list[s - 1] == 0 or ans_list[s - 1] > c:
        ans_list[s - 1] = c
    elif ans_list[s - 1] < c:
        pass
if ans_list[0] == 0:
    print(-1)
    exit()
ans = map(str, ans_list)
print("".join(ans))

"""n, m = map(int, input().split())
ans_list = [0] * n
list1 = []
for i in range(m):
    s, c = map(int, input().split())
    a = [s,c]
    list1.append(a)
    if s == 1 and c == 0:
        ans = -1
    for j in range(i+1):
        if s in list1[j][0] and c == list1[j][1]:
            ans = -1

    ans_list[s - 1] = c
print("\n")
if ans == -1:
    print(ans)
else:
    print(ans_list)
"""
