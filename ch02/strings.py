#Basic print and string functions
name1 = "Bob Willice"
name2 = "ADAM PARORE"

print(name2.title())
print(name1.title())
print(name1.upper())
print(name2.lower())

#Using f to format 
firstName1 = "Bob"
lastName1 = "Willice"

name = f"Hello, {firstName1} {lastName1}!"
print(name)

#rstrip will remove space at the end (or right) of variable name3, use lstrip() for left and strip() from both side
name3 = "Julie "
print(name3+"Hi")
print(name3.rstrip()+"Hi") 