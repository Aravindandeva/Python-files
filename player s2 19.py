n=int(input())
s=[]
w=[]
for i in range(2,n+1):
  if i>1:
    for j in range(2,i):
      if i%j==0:
        break
    else:
      s.append(i)
for k in s:
  if n%k==0:
    w.append(k)

print(*w)
