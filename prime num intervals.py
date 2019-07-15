r,s=map(int,input().split())
for i in range(r+1,s):
  if i>2:
    for j in range(2,r+1):
      if i%j==0:
        break
    else:       
       print(i,end=' ')
  else:
    continue
