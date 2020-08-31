'''
Python script to find triangular series

1
2 + 1 = 3
3 + 3 = 6
4 + 6 = 10
5 + 10 = 15
6 + 15 = 21
7 + 21 = 28
.
.
.

'''


# def nth_triangular(n):
#     triangular = 0
#     for i in range(1, n+1):
#         triangular += i
#     return triangular

triangular = 0
for i in range(1, 101):
    triangular += i
    print(f"[{triangular}]", end=": ")
    for j in range(1, triangular+1):
        if triangular % j == 0:
            print(j, end=", ")
    print()
