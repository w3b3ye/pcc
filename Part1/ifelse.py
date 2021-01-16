#Simple if-else example
cars = ['audi','bmw','toyota','subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#if-else with "not" and "not in"
banned_users = ['Aob','Bob','Dob']
activated_users = []
user = 'Cob'

if user not in banned_users:
    print(f"\nUser {user.upper()} can be activated")
    activated_users.append(user)
if user in activated_users:
    print(f"{user.upper()} has been activated.")