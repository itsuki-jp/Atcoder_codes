def f(n,s):
  if n==0: return print(s)
  for i in 'abc':
    f(n-1,s+i)
f(int(input()),'')