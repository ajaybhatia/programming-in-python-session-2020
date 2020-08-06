# Find simple interest
# SI = (P * R * T) / 100

# p, r, t = 1000, 3.5, 2

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter total period    : "))

si = (p*r*t)/100

print(
    f"Simple Interest of Rs. {p} at the interest rate of {r}% for {t} years is Rs. {si}")
