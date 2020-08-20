'''
Write a script in python to find factorial of a number

4! = 1 X 2 X 3 X 4 = 24
7! = 1 X 2 X 3 X 4 X 5 X 6 X 7 =
'''

num = int(input("Enter a number ? "))
fact = 1

for i in range(1, num+1):
    fact *= i

print(f"Factorial of {num} is {fact}")
