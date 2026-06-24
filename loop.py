# i = int(input("Enter a number grater than 10\n"))
# while i<=10:
#     print("you are correct side")
#     print(i)
#     i = int(input("Enter a number grater than 10\n"))
#     print("Thank you")

# while True:
#     i = int(input("Enter a number to complete divide by 2(0 to exit)"))
#     if i==0:
#         print("Thank you ")
#         break
#     while i>2:
#         i=i/2
#         print(f"Current number is:{i}\n")

print("***********TABLE*************")
i = int(input("Enter a number for Table : "))
for j in range(1,11):
    result=i*j
    print(f"{i}*{j}={result}")

battery_level= 90
while battery_level>0:
    print(f"Battety is running at {battery_level}%")
    battery_level-=5
    if battery_level==5:
        print("please plug in charger")
print("shutdown")