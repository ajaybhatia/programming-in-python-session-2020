'''
Write a script in python to find all multiples of 3, 5 and 7 upto 1 million
'''

for num in range(1, 1000001):
    if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
        print(num, end=",")
