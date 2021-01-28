#Reading a file using 'with'
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

#Reading a file 
file = open('pi_digits.txt','r')
contents = file.read()
print(contents)
file.close()

#When using "with open" you do not need to worry about closing the file though without it you have to close the file by yourself

#Using for loop to read the file
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines() #readlines() method will read the file and create a list with all values
    print(lines)
    for line in lines:
        print(line.rstrip()) #Without using rstrip additional blank lines will be added to the output 

