# Understanding list
print("Creating a list and iterating it using for loop.")
grocery = ['Milk','Salt','Sugar','Rice','Berry']

for g in grocery:
    print(g)

#Various operations with a list like append, del, remove, insert, pop
print("\nVarious operations with a list like append, del, remove, insert, pop")
grocery.append('Cookie')
print(grocery)

del grocery[1] #This will delete "Salt"
print(grocery)

#Calculate square roots using list

print("\nCalculate square roots using list")

#First way of writing code
print("First Method")
squares =[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)

#Second way of writing code
print("Second Method")
squares =[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

#Third way of writing code
print("Third Method, called List Comprehensions")
squares = [value**2 for value in range(1,11)]
print(squares)

#List slicing
print("\nList slicing")
name=['Aob','Bob','Cob','Dob','Eob']
print(name[:3]) #Nothing mentioned before : means it will start from 0, then it will print 0,1,2 items
print(name[1:2]) #Please note that it does not print last one.
print(name[-2:]) #All items are indexed (Right to left) as -5,-4,-3,-2,-1 also.
print(name[:-3]) 

#Looping and List Slicing
print("\nLooping with list slicing")
for n in name[:3]:
    print(n.upper())

#Copying List
print("Copying a list")
my_foods = ['Sandwich','Burger','Pratha']
her_foods = my_foods[:]
his_foods = my_foods

print("My fav food")
print(my_foods)

print("Her fav foods")
print(her_foods)


print("His fav foods")
print(his_foods)

print("Adding another food to my list")
my_foods.append('Filafel')
print("My food: ",my_foods)
print("Her food: ",her_foods) #When using slicing a new list will be created, that is why adding a new item to my_foods does not change this list
print("His food: ",his_foods) #This refer to the my_foods list, hence both are same and changes in any one of them will reflected to both