# countries = ('pakistan','usa','england','bangladesh')
# temp = list(countries)
# temp.append("russia")
# temp.pop(3) #remove item
# temp[2] ="finland"
# countries = tuple(temp)
# print(countries)

# countries2 = ('afganistan','iran','egpet','india')
# southasia = countries+countries2
# print(southasia)

# color = ('black', 'blue','red','green')
# temp = list(color)
# temp.append("Yellow")
# temp.pop(2)
# temp[1] = 'orange'
# color = tuple(temp)
# res = color.count('black')
# print(color)
# print(res)
tuple1= (1,2,34,4,5,6,3,3,36,7,7)
res = tuple1.count(33)
res1 = tuple1.index(3, 4, 9)

print(res,res1)