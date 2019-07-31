i=input()
u=[]
for s in i :
  if(s==('X')):
    u.append('A')
  elif(s=='Y'):
    u.append('B')
  elif(s=='Z'):
    u.append('C')
  else:
    c=ord(s)+3
    u.append(chr(c))
print(*u,sep="")
