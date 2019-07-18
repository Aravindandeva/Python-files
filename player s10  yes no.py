m,n=map(str,input().split())
y=len(n)
count=0
for i in range(0,y):
  if (m[i]==n[i]):
    count+=1
if count==(y-1):
  print('yes')
else:
  print('no')
