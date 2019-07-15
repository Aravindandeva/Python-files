n=str(int(input()))
def myf(n):
  return n[::-1]

f=myf(n)
if n==f:
  print('yes')
else:
  print('no')

