n=int(input())
  
def fact(n):
  if n==1:
    return n
  else:
    return n*fact(n-1)
if n==0:
  print ('1')
else:
  print (fact(n))
