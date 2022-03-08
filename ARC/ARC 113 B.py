# 解説AC
A, B, C = map(int, input().split())
if B == 1:  # Aの1の位をただ出力する
    print(A % 10)
    exit()
if B < 10 and C < 10 and B ** C < 10:  # B^Cが割と小さかったら、普通に計算して出力する
    print(pow(A, pow(B, C), 10))
    exit()
rem = [pow(A, d, 10) for d in range(11)]  # 鳩ノ巣理論
for i in range(10):
    if rem[i] in rem[:i]:
        j = rem.index(rem[i])
        d = i - j
        print(rem[j + (pow(B, C, d) - j) % d])
        exit()
