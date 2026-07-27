# Finally Keyword
# try:
#     l = [1,3,4,5,6]
#     i = int(input("Enter the index :"))
#     print(l[i]) 

# except:
#  print("Some error accur")

# finally:
#    print("I am always excuted")

def func1():
  try:
    l = [1,3,4,5,6]
    i = int(input("Enter the index :"))
    print(l[i]) 
    return 1

  except:
    print("Some error accur")
    return 0

  finally:
   print("I am always excuted")
   
    
x = func1()
print (x)

