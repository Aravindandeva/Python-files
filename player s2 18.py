i=sorted("kabali")
i=str(i)
o=int(input())
a=list()
count=0
for j in range(0,o):
  u=str(input())
  u=sorted(u)
  u=str(u)
  a.append(u)
for h in a:
  if h in i:
    count+=1
print(count)


