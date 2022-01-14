a, b = map(int, input().split())
a_lst = [i for i in range(1, a + 1)]
b_lst = [i * -1 for i in range(1, b + 1)]
diff = sum(a_lst) + sum(b_lst)
if diff == 0:
    print(*a_lst, *b_lst)
elif diff > 0:
    b_lst[-1] = b_lst[-1] - diff
    print(*a_lst, *b_lst)
else:
    a_lst[-1] = a_lst[-1] - diff
    print(*a_lst, *b_lst)
