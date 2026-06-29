mark =[45,46,40,47,41,48,"Qurban",True]
color = ['black','blue','brown','yellow','pink']
fruit =['Apple ','banana','mango','orange','pineapple']
print(color)
print(color[3])
print(len(mark))
print(type(mark))
print(mark)
print(type(mark))
print(mark[2])
print(mark[3])
print(mark[5])
print(mark[7])
print(mark[3]-5)
print(mark[len(mark)-3])
print("The length of color is :",len(color))
print("The length of marks is :",len(mark))
if 46 in mark:
    print("Yes")
else:
    print("Nope")
if 'yellow' in color:
    print("yes")
else:
    print("no")
if "ban" in "Qurban":
    print("Yes")
else:print("No")
print(mark)
print(color)
print(fruit)
print(mark[0:4])
print(mark[0:9:2])
lst = [ i*i for i in range(9)]
lst1 = [ i for i in range(9)]
lst2 = [ i for i in range (18) if i%2==0]
print(lst)
print(lst1)
print(lst2)