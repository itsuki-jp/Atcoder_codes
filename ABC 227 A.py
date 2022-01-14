n,k,a = map(int, input().split())
lst = (list(range(a,n + 1)) + list(range(1,a))) * 1000
print(lst[k - 1])