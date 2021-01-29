filename = 'programming.txt'

#Python can open file in following modes
#'w' - Write mode
#'r' - Read mode
#'a' - Append mode
#'r+' - Read and Write mode
#Default mode is read

with open(filename, 'w') as file_object:
    file_object.write("I am in love with programming, again.\n")
    file_object.write("I love Python this time.\n")

with open(filename, 'r') as file_object:
    print(file_object.read())