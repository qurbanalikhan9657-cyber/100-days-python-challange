#Lec about f string
letter = "My name is {} and i am from {} "
name = "Qurban Khan"
country = "Pakistan"
print(letter.format(name,country))

#Lec about f string
letter = "My name is {1} and i am from {0} "
name = "Qurban Khan"
country = "Pakistan"
print(letter.format(country,name))
print(f" Hey my name is {name} and im from {country}")

# txt = "For only {price:.2f }dollars!"
# print(txt.format(price = 49.545))
price = 49.0999
print(f"For only {price: .2f} dollars")
# print(txt)