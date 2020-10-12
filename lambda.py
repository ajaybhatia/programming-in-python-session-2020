from functools import reduce

number = [10, 45, 23, 90, 56, 34, 100]

# Return one value
x = reduce(lambda total, num: total+num, number)

# Return sublist
y = list(filter(lambda x: x % 5 == 0, number))

# Return list
z = list(map(lambda x: x+10, number))
print(z)
