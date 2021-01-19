#Modifying a list with 'while' loop
print("Modifying a list with 'while' loop.")
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'] 
print(pets) 

while 'cat' in pets: 
    pets.remove('cat') 
    
print(pets)

#Modifying a lost with 'for' loop
print("Modifying a list with 'for' loop.")
pets_1 = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'] 
print( pets_1) 

for pet in pets_1: 
    if pet == 'cat':
        pets_1.remove('cat') 

print(pets_1)