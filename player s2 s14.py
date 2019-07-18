u=int(input())
p=str(input())

o=['a','e','i','o','u']
for i in p:
  if i in o:
    p=p.replace(i,'')
print(p[::-1])
