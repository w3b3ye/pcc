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
squares =[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)

 