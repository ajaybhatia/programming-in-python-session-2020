'''
Python script to find whether a number is prime or not
'''

num = int(input('Enter any number: '))
is_prime = True

# Test
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")
