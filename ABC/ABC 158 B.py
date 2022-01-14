s = input()

s_norm = list(s)
s_rev = list(reversed(s))
if s_norm == s_rev:
    s_len = len(s)
    second = round((s_len -1)/2)
    s_new = s_norm[0:second]
    s_new_rev = list(reversed(s_new))
    if s_new == s_new_rev:
        third = round((s_len +3)/2)
        s_last = s_norm[third-1:s_len+1]
        s_last_rev = list(reversed(s_new))
        if s_last == s_last_rev:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")

