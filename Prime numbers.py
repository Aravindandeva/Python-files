print("Choose from the following Options Of Displaying Prime Numbers as 1 or 2 ",end='\n')
print("""1-List of Prime Numbers from specific Range,
2-Check wheather a given number is prime or not  """)
a=int(input("Enter the Option-"))
if(a==1):
  lower=int(input("enter the lower range - "))
  higher=int(input("enter the higher range -"))
  def primenumber():

      for num in range (lower,higher+1):
        if(num>1):
          for i in range(2,num):
            if((num%i) == 0 ):
                break
          else:
              print(num,end=" ")
             
              
               
  primenumber()
          
        

           
      
      
      

if(a==2) :
  
  b=int(input("Enter a Number greater than 1"))
  for i in range(2,b) :
    if((b%i)==0):
      print(num,"is not a prime number")
      break
    else:
      print("Entered number is a prime number")
        
    



        

