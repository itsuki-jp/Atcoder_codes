n = int(input())
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ans = []
for i in range(1,99):
    if n <= 26 ** i:
        n -= 1
        for j in range(i):
            alp = n %26
            ans.append(alphabet[alp])
            n //= 26
        break
    else:
        n -= 26 ** i
print("".join(ans[::-1]))