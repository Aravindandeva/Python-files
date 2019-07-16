ino=int(input())
def fact(ino):
  if ino==0:
    return 1
  else:
    return(ino*fact(ino-1))
print(fact(ino))
