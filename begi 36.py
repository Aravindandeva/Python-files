u=str(input())
count=0
for i in u:
  if (i.isalnum()):
    count+=1
t=len(u)
y=abs(count-t)
print(y)
