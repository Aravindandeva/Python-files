u=int(input())
p=str(input())

o=['a','e','i','o','u','A','E','I','O','U']
for i in p:
  if i in o:
    p.replace(i,'')
print(p[::-1])

