print("*****************WELCOME*****************")
# while True :
a = float(input("Enter the num1:"))
b = int(input("Enter the num2: "))
x = input("Enter the operation you want to perform +,-,*,/")
match x:
    case '+' :
         print("The sum of ",a,"and",b, "is",a+b)
    case '-':
           print("The diff of ",a,"and",b, "is",a-b)
    case'*':
           print("The multiple of ",a,"and",b, "is",a*b)
    case'/':
             print("The divide of ",a,"and",b, "is",a/b)
    case _:
              print("invaild opertion") 
again = input("Do you want to use our calclator y/n.?").lower()
if again != 'y':
       print("Thanks..........")

import time
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))
print(f"current time:{hour:2d}:{minute:2d}:{second:2d}")

print("********************************************")
s = int(input("Enter a number"))
if (s==0):
       print("number is zero")
elif(s<10):
       print("The number is less than 10")
elif(s<100):
        print("The number is less than 100")
elif(s<1000):
        print("The number is less than 1000")
elif(s<10000):
        print("The number is less than 10000")
elif(s<100000):
        print("The number is less than 100000")
elif(s<1000000):
        print("The number is less than 1000000")
else:
       print("The number is greater than one millon")