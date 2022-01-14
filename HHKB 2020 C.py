n = int(input())
p = list(map(int,input().split()))
lst = [0 for _ in range(max(p))] + [0] + [0]
ans = 0

for i in p:
    if i > ans:
        if lst[i] == 0:
            print(ans)
            lst[i] = 1
        elif i!=ans:
            print(ans)
    else:
        if i!=ans:
            print(ans)
        else:
            j = 1
            lst[i] = 1
            while lst[ans+j] != 0:
                j += 1
            ans += j
            print(ans)