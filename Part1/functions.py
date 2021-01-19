#A simple function with parameter 
def greet(username): #Here username is called as parameter 
    """Display a simple greeting."""
    print(f"Hello,{username.title()}!")

greet('Bob') #Here is passed to function. 'Bob' is called as arguments 

#Another function example
def  about_pet(pet_name,animal_type='tiger'): #Parameter with default value should be mentioned at the end 
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

about_pet(animal_type='dog',pet_name='tiger') #Sequence does not matter when using parameter name with arguments
about_pet(pet_name='tommy') #We have not passed animal_type, python will take the default value

#One more function example
def formatted_name(first_name,last_name,middle_name=''): #middle_name is optional parameter here 
    """Return a full name, well formatted."""
    if middle_name:
        full_name = f"\n{first_name} {middle_name} {last_name}"
    else:
        full_name = f"\n{first_name} {last_name}"
    return full_name.title()

print(formatted_name('jimi','hendrix')) 
print(formatted_name('jimi','hendrix','lee'))  

#Return a dictionary 


def user_details(first_name,last_name,age=None):
    """Retrun a dictionary with user details"""
    person = {'first':first_name,'last':last_name}
    if age:
        person.update({'age':age})
        #person['age'] = age
    return person

user = user_details('jimi','hendrix',age=27)
print(user)

print(user_details('mimi','vendrix'))


    