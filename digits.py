"""
A simple numbers calculator.
"""

print('Staring calculator ...')
print('(Enter everything except numbers to quit.)')
digits = []

def calc():
	result = 0	
	for digit in digits:
		result += digit
	return result

while True: 
	user_input = input("Enter a number: ")
	try:
		number = int(user_input)
		digits.append(number)
		print('Current sum is: ', calc())

	except ValueError:
		print("Error")
		break
