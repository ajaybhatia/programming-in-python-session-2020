# Bitwise Operators
# | (Bitwise OR)
# & (Bitwise AND)
# ^ (Bitwise XOR)
# ~ (Bitwise NOT)
# << (Bitwise Left Shift)
# >> (Bitwise Right Shift)

x, y = 11, 3

# 11 => 1011
# 3  => 0011
#       ----
#       1011 => 11
#       ----
# | (Bitwise OR)
print(x | y)

# 11 => 1011
# 3  => 0011
#       ----
#       0011 => 3
#       ----
# & (Bitwise AND)
print(x & y)

# 11 => 1011
# 3  => 0011
#       ----
#       1000 => 8
#       ----
# ^ (Bitwise XOR)
print(x ^ y)

# 11 => 1011 =>  .....11111111111110100
# 11 => 11 + 1 = 12 => -12
# ~ (Bitwise NOT)
print(~x)

# << (Bitwise Left Shift)
# x << y = x * 2**y
print(x << y)

# >> (Bitwise Right Shift)
# x >> y = x // 2**y
print(x >> y)
