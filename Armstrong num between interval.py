n,u=map(int,input().split())
for i in range(n,u):
  sum=0
  ru=i
  while ru>0:
    te=ru%10
    sum=sum+te**3
    ru=ru//10
    if sum==i:
      print(i)
    
