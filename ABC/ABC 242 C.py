mod = 998244353
n = int(input())
lst = [2, 3, 3, 3, 3, 3, 3, 3, 2]
if n == 2:
    exit(print(25))

for i in range(n - 2):
    n_lst = [0 for _ in range(9)]
    n_lst[0] = lst[0] + lst[1]
    n_lst[1] = sum(lst[:3])
    n_lst[2] = sum(lst[1:4])
    n_lst[3] = sum(lst[2:5])
    n_lst[4] = sum(lst[3:6])
    n_lst[5] = sum(lst[4:7])
    n_lst[6] = sum(lst[5:8])
    n_lst[7] = sum(lst[6:9])
    n_lst[8] = lst[7] + lst[8]
    lst = [n_lst[_] % mod for _ in range(9)]
print(sum(lst) % mod)


