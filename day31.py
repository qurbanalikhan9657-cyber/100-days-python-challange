# SETS
# we are studing about sets 
# its start with curly braket
s = {2,3,4,2,5,6,7}
print(s)

info = {"carlo",8 , "fast ", True,5.9,19,8}
print(info)

# qurban = {}
qurban = set()
print(type(qurban))
for value in info:
    print(value)


#example of sets in python



fruits = {"mango","banana","apple","cherry","mango"}
fruits.add("orange")
fruits.remove("mango")
print(fruits)


# EXAMPLE 2
ban_ips = {"192.10.1","192.11.0","192,12.1"}
x = input("Enter the ip: ")
if x in ban_ips:
    print("Access DENIED!!!!")
else:
    print("WE are forworded to our mission")