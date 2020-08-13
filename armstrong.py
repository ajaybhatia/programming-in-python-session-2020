# Progrm to find whether the number is armstrong

# 153 = 1**3 + 5**3 + 3**3 = 1 + 125 + 27 = 153

num = int(input("Enter three digit number: "))

d3 = num % 10
d2 = (num // 10) % 10
d1 = num // 100

prop_arm = d1**3 + d2**3 + d3**3

if prop_arm == num:
    print(f"{num} is armstrong number")
else:
    print(f"{num} is not armstrong number")
