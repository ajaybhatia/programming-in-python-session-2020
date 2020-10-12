'''
Highly composite numbers

1: 1
2: 1, 2
4: 1, 2, 4
6: 1, 2, 3, 6
12: 1, 2, 3, 4, 6, 12
24: 1, 2, 3, 4, 6, 8, 12, 24

Write a python script to find all HCN below 100000
Hint: All HCN are even numbers
'''


def factors_count(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return count


prev_factors = 0
for num in range(1, 100001):
    # Logic to check a number whether
    # it is even or odd. If the number
    # is odd then it cannot be HCN
    if num == 1 or num % 2 == 0:  # Test for Even number
        current_count = factors_count(num)
        if current_count > prev_factors:
            prev_factors = current_count
            print(num)
