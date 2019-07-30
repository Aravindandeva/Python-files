a,b=map(int,input().split())
i=2
while(i>0):
  if(i%a == 0 and i%b == 0):
    print(i)
    break
  i=i+1


