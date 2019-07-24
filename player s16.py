o=int(input())
j=list(map(int,input().split()))



for i in j:
  if (j.count(i))<=1:
    
    ans=i
print(ans)
