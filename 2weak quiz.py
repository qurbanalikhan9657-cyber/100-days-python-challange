# ​Question 1: Write a program that prints your name, age, and favorite hobby on three separate lines using a single print() statement.

print("My name is Qurban khan\n I am 19 years old\n My favorite hobby is coding\n")

# ​Question 2: Create variables to store the following values: 100, 99.9, "Python", and True. Print the data type of each variable using a built-in Python function.

var1 = 100
var2 = 99.9
var3 = "python"
var4 = True
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4),"\n")

# ​Question 3: What is the difference between a multi-line comment and a multi-line string in Python? Write an example of both.

# A multi-line comment is used to add comments that span multiple lines and is typically enclosed within triple quotes (''' or """). It is ignored by the Python interpreter and is used for documentation or explanations in the code.

# ​Question 4: Create a program that asks the user to enter two numbers. Multiply these numbers together and print the result. (Hint: Remember to handle the data type of the user input!)

x = int(input("Enter num1:"))
y = int(input("Enter num2:"))
print("The multiplication result of ",x,"and",y ,"is:",x*y,"\n")

# ​Question 5: Write a program that takes a floating-point number as input from the user and converts it into an integer. Print both the original value and the converted integer value.

x = float(input("Enter a float number:"))
print("The number in float is:",x)
print("The number in int is :",int(x),"\n")

# ​Question 6: Ask the user for their birth year, calculate their approximate age, and print: "You are X years old." (Assume the current year is 2026).

x = int(input("Enter your brithday year:"))
print("your are: ",2026-x,"years old","\n")

# ​Question 7: Given the string text = "Python Programming Is Fun", write the code to:
# ​Print only the word "Programming" using string slicing.
# ​Print the entire string in all lowercase letters.
# ​Replace the word "Fun" with "Awesome".

str = "Python Programming Is Fun"
print(str[7:18])
print(str.lower())
print(str.replace("Fun","awesome"))

# ​Question 8: Take a string input from the user and print the total number of characters it contains (including spaces).

x = (input("Enter the string:\n"))
len1 =len(x)
print("The number of character in string is:",len1,"\n")

# ​Question 9: What will be the output of the slicing expression mystr[-5:] if mystr = "Hello World"?

# out put will be "WORLD"
mystr = "Hello World"
print(mystr[-5:], "\n")

# ​Question 10: Write a program that asks the user for a number and checks whether it is even or odd. Print an appropriate message for both cases.

x = int(input("Enter a number:"))
if x %2==0:
 print("The number is even\n")
else:
 print("number is odd\n")

 # ​Question 11: Create a grading system program. Ask the user to input their exam score (out of 100):
# ​Score >= 90: Print "Grade A"
# ​Score >= 80 and < 90: Print "Grade B"
# ​Score >= 70 and < 80: Print "Grade C"
# ​Score < 70: Print "Fail"

x = int(input("Enter your marks:"))
if x>=90:
 print("Grade A+\n")
elif x>80 and x<=90:
 if x>85 and x<=90:
  print("A- Grade\n")
 else:
  print("Grade B\n")
elif x>70 and x<=80:
 print("Grade C\n")
else:
 print("F Grade\n")

 # ​Question 12: Write a script that asks the user to enter the current hour of the day (in 24-hour format, from 0 to 23).
 # ​If the hour is between 5 and 11, print "Good Morning".
# ​If the hour is between 12 and 17, print "Good Afternoon".
# ​Otherwise, print "Good Evening".

x = int(input("Enter the current hour of day from 00 t0 23:" ))
if x>=8 and x<=11:
 print("Good Morning sir\n")
elif x>11 and x<=17:
 print("Good afternoon\n")
elif x>17 and x<=19:
 print("Good Evening\n")
else:
 print("Good night\n")

#Example 2

import time
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))
print(f"current time: {hour:02d}:{minute:02d}:{second:02d}")
if hour>=8 and hour<=11:
 print("Good Morning sir\n")
elif hour>12 and hour<=17:
 print("Good afternoon\n")
elif hour>17 and hour<=19:
 print("Good Evening\n")
else:
 print("Good night\n")
  
# ​Question 13: Write a program using a match-case statement that asks the user to enter a number from 1 to 7 and prints the corresponding day of the week (e.g., 1 for Monday, 2 for Tuesday, etc.). Include a default case that prints "Invalid day" if they enter any other number.

x = int(input("Enter a number from 1 to 7 and prints the corresponding day of the week:\n"))
match x:
 case 1:
  print("Monday")
 case 2:
  print("Tuesday")
 case 3:
  print("wednesday")
 case 4:
  print("Thursday")
 case 5:
  print("Friday")
 case 6:
  print("saturday")
 case 7:
  print("Sunday")
 case _:
  print("Invaild day")

  # ​Question 14: Use a match-case statement to simulate a simple menu. Ask the user to choose an option: 'A' for "Add User", 'B' for "Delete User", and 'C' for "Exit". Print the corresponding action based on their choice. Make sure it handles both uppercase and lowercase inputs (e.g., 'a' or 'A').

print("****Menu****")
x = input(("A = Add user\nB = Remove user\nC = Exit\n" ))
match x :
 case 'A'| 'a':
  print("Add action\n")
 case 'B'| 'b':
  print("Remove action\n")
 case 'C'|'c':
  print("Exit action\n")
 case _:
  print("Invaild action\n")
