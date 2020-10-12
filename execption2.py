# Program to find factorial of a natural number (1 - +ve infinity)

def fact(n):
	if n == 1:
		return 1
	else:
		return n*fact(n-1)

try:
	x = int(input("Enter a number: "))
	if x <= 0:
		raise Exception(f"{x} is not natural number")
	print(f"Factorial of {x} is {fact(x)}")
except ValueError:
	print("You entered wrong number format")
except:
	print("Number cannot be less than or equal to 0")