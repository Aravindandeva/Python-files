nu=int(input())
sum=0
ru=nu
while ru>0:
 te=ru%10
 sum=sum+te**3
 ru=ru//10
if sum==nu:
  print('yes')
else:
  print('no')
