'''
Polygon Number

Ref: https://en.wikipedia.org/wiki/Polygonal_number

Formmula to find nth s-gonal number:
P(s, n) = ((s-2)*n**2 - (s-4)*n) / 2
'''


def nth_s_gonal_number(s, n):
    return ((s-2)*n**2 - (s-4)*n) // 2


# First 100 Pentagonal Numbers
# for i in range(1, 101):
#     print(nth_s_gonal_number(5, i))


# First 100 Hexagonal Numbers
for i in range(1, 11):
    print(nth_s_gonal_number(6, i), end=",")
