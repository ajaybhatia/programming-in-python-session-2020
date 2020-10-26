__version__ = "1.0.0"

def is_pos(number):
	return number > 0

def is_neg(number):
	return not is_pos(number)

def is_zero(number):
	return number == 0

def is_prime(number):
	if number == 2 or number == 3:
		return True
	if number % 2 == 0:
		return False
	for i in range(2, int(number**0.5)+1):
		if number % i == 0:
			return False
	return True	

def is_armstrong(number):
	d3 = number % 10
	d2 = (number // 10) % 10
	d1 = number // 100
	return d1**3+d2**3+d3**3 == number

def gen_armstrong_numbers():
	for number in range(100, 1000):
		temp, sum = number, 0
		while temp > 0:
			d = temp%10
			sum += d**3
			temp //= 10
		if sum == number:
			print(number)


def gen_narcisstic_numbers(limit):
	for number in range(1, limit+1):
		temp, sum, size = number, 0, len(str(number))
		while temp > 0:
			d = temp%10
			sum += d**size
			temp //= 10
		if sum == number:
			print(number)