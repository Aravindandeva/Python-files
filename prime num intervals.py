r,s=map(int,input().split())
for num in range(r+1,s):
  if num>1:
    for j in range(2,num):
      if num%j==0:
        break
    else:       
       print(num,end=' ')
  
