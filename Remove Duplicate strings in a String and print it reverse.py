a=input()
v=""
for i in a:
  if v == "" or i!=v[len(v)-1]:
    v+=i
print(v[::-1])
