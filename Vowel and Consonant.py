lis=['a','e','i','o','u']
ch=str(input().casefold())
if (ch>'a' and ch<'z'):
  if ch in lis :
    print('Vowel')
  else:
    print('Consonant')
else:
  print('invalid')
