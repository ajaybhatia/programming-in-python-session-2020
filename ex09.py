'''
1 = 1
2 = 2**2/2!
3 = 3**3/3!
4 = 4**4/4!
..
..
..
'''


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


def term(n):
    return n**n//factorial(n)


for i in range(1, 101):
    print(term(i))
