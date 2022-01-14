n,k = map(int,input().split())
x = list(map(int,input().split()))

lst_sum = [sum[:k]]

for i in range(1,n-k):
    lst_sum[i] = lst_sum[i-1] + abs(x[k] - x[k+i]) 