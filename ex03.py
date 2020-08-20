'''
Write a script in python to find all armstrong numbers

Armstrong Numbers
All those three digit numbers whose sum of qube of each digit is equals to the number

153 = 1**3 + 5**3 + 3**3 = 153

d1 = 153 % 10 = 3
d2 = 153 // 10 = 15 % 10 = 5
d3 = 153 // 100 = 1
'''

for num in range(100, 1000):
    d1 = num % 10
    d2 = num // 10 % 10
    d3 = num // 100

    sum = d1**3 + d2**3 + d3**3

    if num == sum:
        print(num)
