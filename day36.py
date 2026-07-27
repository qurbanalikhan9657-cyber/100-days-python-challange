# Python Error Handling
# Expection Handling

# a = input("Enter a number ")
# print (f"Multiplication table of {a} is:")
# try:
#      for i in range (1,11):
#     print(f"{a}*{i}= {int(a)*i}"
#           except as e:
#           print(e)
          


# a = input("Enter a number ")

# print (f"Multiplication table of {a} is:")
# try:
# for i in range (1,11):
#     print(f"{a}*{i}= {int(a)*i}"
#           except as e:
#           print(e)
# print("some lines of code ")
# print("Ending of our program")

a = input ("Enter a number ")
print(f"Multiplication of {a} is :")
try:
    for i in range (1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
  print(e)
print("some important lines of code")
print ("End of code")

#Example 2

a = input("Enter tempreture in Calcus ")
try:
   b = 9/5 * int(a) + 32
   print(f"{int(a)} Tempreture in F is : {b} F ")
except Exception as e:
  print(e)

print("May be you have enter a wrong value ")
print("Our program skip and do expection handling")

# Example 3 
try:
  num = int(input("Enter an integer  "))
  a = [5,6] 
  print(a[num])
except ValueError:
   print("number entered is not an integer")
except IndexError:
   print("Index error")
