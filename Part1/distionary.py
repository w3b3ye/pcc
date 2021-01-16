#A simple dictionary example
fav_language = {
    'jen': 'c',
    'sarah': 'python',
    'edward': 'ruby',
    'phil': 'java',
}

print("Printing keys and values separately.")
for name in fav_language.keys():
    print(name.title())

for lang in fav_language.values():
    print(lang.title())

print("\n Printing keys and values togerther.")
for name, value in fav_language.items():
    print(f"{name.title()} loves {value.title()}.")

#A list within a dictionary

fav_languages = {
    'jen': ['c', 'c#'],
    'sarah': ['python'],
    'edward': ['ruby', 'java', 'c++']
}

for name, languages in fav_languages.items():
    print(f"\n{name.title()}'s fav languages are.")
    for language in languages:
        print(f"\t{language.title()}") 

#A dictionary within a dictionary

users = {
    'user1':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'user2':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username.title()}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    