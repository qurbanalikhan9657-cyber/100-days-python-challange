functions
a = 5
b = 9
gmean = (a*b)/(a+b)
print (gmean) 
c = 34
d = 12
gmean1 = (c*d)/(c+d)
print (gmean1) 
def average(*args):
     if not args:
          return 0
     return sum(args)/ len(args)
print(average(2.3,43,53,43.3))

def Gmean (a,b):
    mean = (a*b)/(a+b)
    print(mean)
def isGreater(a,b):
      if (a>b) :
           print("first number is greater")
      elif (a==b):
           print("Both number are equal")
      else: 
           print("Second number is greater ")
def add(a,b):
     add=(a+b)
     print(add)
def sub(a,b):
     print("the subtraction of ",a,"and",b,"is: ",a-b)
def mul(a,b):
     print("the multiplication of ",a,"and",b,"is: ",a*b)
a = 9
b = 13
Gmean(a,b)
isGreater(a,b)
c = 34
d = 12

isGreater(c,d)
Gmean(c,d)
add(c,d)
sub(c,d)
mul(c,d)
min(c,d)
max(c,d)
average()
