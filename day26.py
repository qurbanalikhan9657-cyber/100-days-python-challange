import time
hour= int(time.strftime('%H'))
print("Current hour is :",hour)
min = int(time.strftime('%M'))
print("Current miniute is :",min)
sec= int(time.strftime('%S'))
print("Current second is :",sec)
if hour >0 and hour<=9:
    print("Good Morning sir")
elif hour<15 and hour>9 :
 print("Good afternoon")
else:
   print("good night")
# timestamp1 = time.strftime('current date %D-%m-%Y')
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
# print(timestamp1)
