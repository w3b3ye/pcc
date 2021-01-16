#A dictionary example
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

