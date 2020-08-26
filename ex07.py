'''
Write a script in python to find all narcisstic numbers upto 1 million

0 = 0**1 = 0
1 = 1**1 = 1
..
..
9 = 9**1 = 9
10 = 1**2 + 0**2 = 1 + 1 = 2 Not narcisstic
.
.
.
1234 = 1**4 + 2**4 + 3**4 + 4**4 = 1 + 16 + 81 + 256 = 354 Not narcisstic

5 = 5**1 = 5
25 = 2**2 + 5**2 = 4 + 25 = 29 Not narcisstic
'''

for num in range(1, 1000001):
    # Check whether num is narcisstic or not
    temp, sum, size = num, 0, len(str(num))
    while temp > 0:
        d = temp % 10
        sum += d**size
        temp //= 10

    if sum == num:
        print(num)
