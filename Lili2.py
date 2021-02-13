def number_length(num):
	# Set initial lenght value to 0
	length = 0
	# Divide by 10 (use // instead of / to do integer divission instead of float point division)
	# This will reduce num by one digit each iteration
	# Add one to length each iteration
	while num > 0:
		num = num // 10
		length = length + 1

	return length


def list_of_multiples(num, length):
	# Return empty list if length value is None
	if length is None:
		return []

	else:
		# Create empty multiples list
		multiples = []
		"""" We need to find multiples of num. For example, if we are finding multiples of 3
		we would need to add 3*1, 3*2, 3*3, 3*4, etc to the muliples list."""
		for i in range(1, length + 1):
			multiple = num * i
			multiples.append(multiple)

		return multiples


def normalize(input_str):
	# Check if input string is uppercase
	if input_str.isupper():
		# Convert string to captialized with and add an exclamation point to the end
		input_str = input_str.capitalize()
		input_str = input_str + '!'

	return input_str
		

def cat_dog(num):
	# Return CatDog if num is evenly divisible by 3 and 5
	if num % 3 == 0 and num % 5 == 0:
		return 'CatDog'
	# Return Cat if num is evenly divisible by 3
	elif num % 3 == 0:
		return 'Cat'
	# Return Dog if num is evenly divisible by 5
	elif num % 5 == 0:
		return 'Dog'
	# Convert num to a string and return it
	else:
		return str(num)


print('Enter a number to get its length: ')
num = int(input())
print(number_length(num))

print('Enter a number to receive multiples of: ')
num = int(input())
print('How many multiples do you want?')
length = int(input())
print(list_of_multiples(num, length))

print('Please enter a string to normalize: ')
input_string = input()
print(normalize(input_string))

print('Please enter a number: ')
num = int(input())
print(cat_dog(num))
