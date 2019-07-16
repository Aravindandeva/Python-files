ino=int(input())


def fact(ino):
  if ino==0:
    print("1")
  else:
    print(ino*fact(ino-1))
print(fact(ino))
