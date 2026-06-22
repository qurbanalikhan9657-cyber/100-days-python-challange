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
p   print("Number is between 10 to twenty")
else:
   print ("This number is out of range")rint(a!=18)
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
    
q = int(input ("Enter your Marks in percentage"))
if(q==100):
    print("excellent")
elif(q>=90):
     if(q<90 and q>80):
        print("very good")
        if(q>=80 and q>70):
            print("good")
            if(q>=70 and q>60):
                print("average")
                if(q>=60 and q>50):
                    print("below average")
                    if(q>=50 and q>40):
                        print("poor")
                        if(q>=40 and q>30):
                            print("very poor")
                            if(q>=30 and q>20):
                                print("fail")
                               