u=str(input())
count=0
for i in u:
  if (i.isalnum()):
    count+=1
t=len(u)
print(count-t)
