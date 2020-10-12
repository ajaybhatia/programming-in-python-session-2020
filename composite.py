'''
List all composite numbers till 1000
'''


def is_prime(num):
    if num == 1 or num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True


for num in range(1, 1001):
    if (not is_prime(num)):
        print(num, end=", ")
