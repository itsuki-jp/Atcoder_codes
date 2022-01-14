s = input()
ans = "Yes"
if len(s) %2 == 0:
  for i in range (len(s)):
    if i % 2 ==0 and s[i] != "h":
        ans = "No"
        break
    elif i % 2 ==1 and s[i] != "i":
        ans = "No"
        break
print(ans)