for n in range(1, 20):
    l = len(str(n))
    mod = 998244353
    past = 0
    nine = 9
    past_nine = 0
    for i in range(l):
        if i != (l - 1):
            past += (1 + nine - past_nine) * (nine - past_nine) / 2
            past_nine = nine
            nine *= 10
            nine += 9
        else:
            ans = past + (1 + n - past_nine) * (n - past_nine) / 2
            print(int(ans) % mod)
