o=int(input())
lis=list(map(int,input().split()))
i=0
j=o-1
lis=sorted(lis)
def arrsort(lis,o):
  i=0
  j=o-1   
  while(i<j):
    print(lis[j],end=" ")
    print(lis[i],end=" ")
    i+=1
    j-=1
  if ((o%2) !=0 ):
    print(lis[i])
arrsort(lis,o)
