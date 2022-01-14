def Base_10_to_n( X, n ):
    if int(X / n):
        return Base_10_to_n(int(X / n), n) + str(X % n)
    return str(X % n)


k = int(input())
ans = bin(k)[2:]
print(ans.replace("1", "2"))