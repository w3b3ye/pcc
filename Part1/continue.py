#Print Odd numbers using continue

num = 0
while num <10:
    num = num + 1
    if num % 2 == 0:
        continue
    print(num)