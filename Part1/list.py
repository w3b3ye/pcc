# Understanding list
print("Creating a list and iterating it using for loop.")
grocery = ["Milk","Salt","Sugar","Rice","Berry"]

for g in grocery:
    print(g)

#Various operations with a list like append, del, remove, insert, pop
print("\nVarious operations with a list like append, del, remove, insert, pop")
grocery.append("Cookie")
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
print("List slicing")
name=['Aob','Bob','Cob','Dob','Eob']
print(name[:3]) #Nothing mentioned before : means it will start from 0, then it will print 0,1,2 items
print(name[1:2]) #Please note that it does not print last one.
print(name[-2:]) #All items are indexed (Right to left) as -5,-4,-3,-2,-1 also.
print(name[:-3]) 