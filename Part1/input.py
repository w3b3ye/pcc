# To check even or odd

num = input("Enter a number to check if it is even or odd:")
num = int(num)

if num % 2 == 0:
    print(f"\nThe number {num} is even.")
else:
    print(f"\nThe number {num} is odd.")