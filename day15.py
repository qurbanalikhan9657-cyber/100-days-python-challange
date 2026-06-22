# import os
# print("Hello from...")
# os.system("python --version")
x = int(input("Enter a number"))
match x:
    case 0:
        print("x is zero")
    case 4 if x % 2==0:
        print(" x % 2==0 and case is 4")
    case _ if x < 10:
        print("x is less than ten")
    case _ if x < 100:
        print("The given number is less than 100")
    case _ if x < 1000:
        print("number is less than 1000")
        
