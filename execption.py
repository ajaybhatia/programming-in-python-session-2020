x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Exception Handling
try:
	print(f"{x} divide by {y} is {x/y}")	
except:
	print(f"{x} cannot be divided by zero")
finally:
	print(f"{x} times {y} is {x*y}")