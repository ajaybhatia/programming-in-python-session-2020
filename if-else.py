# 1. if statement
# 2. if else statement
# 3. if elif else statement


# To check whether a given number is even
num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"{num} is even")


# To check whether a given number is even or odd
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# To check whether a number is negative, positive or zero
if num < 0:
    print(f"{num} is negative number")
elif num > 0:
    print(f"{num} is positive number")
else:
    print(f"{num} is zero")
