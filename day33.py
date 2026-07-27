# Day 33

dict = { 
    "Qurban" :"Human being",
    "Spoon"  :"An object"
}

sib = {
    1:"Qurban Khan",
    "2": "Irfan khan",
    "3": "Zeeshan Khan",
    "4": "Ahsan Khan"
}

# we can save number in dic like string also as int so we will also recall it as we have save it before


print(dict["Qurban"])
print(sib[1])
print(sib["3"])
print(sib["2"])
print("******Empolyee ID*****")


emp = {
    101:"ABBAS",
    102:"Ali Hassan",
    103:"Akbar ali",
    104:"Zafar jamali"
    }
print(emp[104])

info ={
    'name ': 'Qurban',
    'age' : '19',
    'eligible':True
}
# print(info["name "])
# print(info["age"])
# print(info.get("eligible"))
for key in info.keys():
    print(info[key])
# print(info.keys())



