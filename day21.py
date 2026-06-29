def average(*numbers):
    sum =0
    for i in numbers:
          sum = sum+i
    #print("The average of number is :",sum/len(numbers))
    return sum/len(numbers)
c = average(23,26,29)
print(c)

def addition(*numbers):
     sum = 0
     for i in numbers:
          sum = i+sum
     print("The sum of numbers is :",sum)
addition(43,24,2432,434,43)

def diffrence(*numbers):
     diff=0
     for i in numbers:
          diff= i-diff
     print("the diffrence of number is:",diff)
diffrence(86,40 )
 
def mul(*numbers):
     mul =1
     for i in numbers:
         mul = mul*i
     print("The multipliction of numbers is :",mul)

mul(23,2)

def name(**name):
     print("Hello,",name["fname"],name["mname"],name["lname"])

name(mname="ali",lname="khan",fname="Qurban")
def average(*numbers):
     sum =0
     for i in numbers:
          sum = sum+i
     print("Average of numbres is :",sum/len(numbers))
average(23,26,29)
