#Print Odd numbers using continue

num = 0
while num <10:
    num = num + 1
    if num % 2 == 0:
        continue #If number is even continue will break the loop and start from beginning again
    print(num)

