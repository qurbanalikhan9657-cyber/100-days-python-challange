import time

hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))

print(f"Current time: {hour:02d}:{minute:02d}:{second:02d}")

if 5 <= hour < 12:
   print("Good morning sir")
elif 12 <= hour < 17:
   print("Good afternoon sir")
elif 17 <= hour < 21:
   print("Good evening sir")
else:
   print("Good night sir")
