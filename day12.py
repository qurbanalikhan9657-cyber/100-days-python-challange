#strig are inmuteable 
#in this lecture we will learn about string case
a = "Qurban"
b = "!!!Qurban!!!!!!!!!!!!!!!!!!!!!"
c = "QUn R B A N"
d = "we are learning pyThon by code with harry and it is our dA y 12 and We are manTaining our streak daily have work on it "
e = "hey this string is for count method. Who are you ? . What is you ? Why are you?"
str = "Welcome to console"
f = "hello world"

print(len(a))
print(type(a))
print(a[3:5])
print(a[0:6])
print(a.upper())
print(b.lower(),a.rstrip("!"))
print(a.capitalize())
print(b.rstrip("!"))
print(a.replace("Qurban","Khan"))
print(b.replace("Qurban","Ali"))
print(c.split(" "))
print(d.capitalize())
print(str.center(50))
print(len(str))
print(len(str.center(50)))
print(e.count("you"))
print(e.endswith("?"))
print("Example of endwith")
print(e.endswith("@@"))
print(e.endswith("to",))
print(e.find("is"))
print(a.isalnum())
print(e.isalpha())
print(a.isalpha())
print(f.islower())
print(f.isprintable())
print(f.isspace())
print(e.swapcase())
