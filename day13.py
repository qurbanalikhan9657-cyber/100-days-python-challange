#  if-else statement

#Example 1

c = int(input("enter your budget"))
applePrice = 200
budget = c
if (applePrice <= c):
  print("you can buy apple")
else:
  print("Your budget is low")

  #Example 2

a = int(input("enter you age :"))
print("your age is :",a)
print(a>18)
print(a<18)
print(a==18)
print(a!=18)
if(a>=18):
  print("you can drive")
else:
  print("you cannot drive") 
  print("yes in else")

  #Example 3

num = int(input("Enter the value for num:"))
if(num<0):
    print("num is negative")
elif(num==0):
    print("num is zero")
elif(num==777):
   print("You got lucky number")
elif(num==45):
   print("Random number")
else:
    print("num is positive")
print("iam happy now")

#Nested if example 4

num1 = int(input("Enter the number"))
if (num1<0):
   print("number is negtive")
elif(num1>0):
   if (num1<=10):
    print("number is between 10")
   elif(num1>=10 and num1<20):
       print("Number is between 10 to twenty")
else:
   print ("This number is out of range")
q = int(input ("Enter your Marks in percentage"))
if(q==100):
    print("excellent")
elif(q>=90):
     if(q<90 and q>80):
       print("A")
     elif(q>70):
       print("B")
