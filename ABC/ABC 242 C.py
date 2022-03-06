mod = 998244353
n = int(input())
lst = [1 for _ in range(9)]

# 791ms
for i in range(n - 1):
    n_lst = [0 for _ in range(9)]
    for j in range(9):
        if j == 0:
            n_lst[0] = lst[0] + lst[1]
        elif j == 8:
            n_lst[8] = lst[7] + lst[8]
        else:
            n_lst[j] = sum(lst[j - 1:j + 2])

    lst = [n_lst[_] % mod for _ in range(9)]
print(sum(lst) % mod)
