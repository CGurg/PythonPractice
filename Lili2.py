def number_length(num):

	length = 0

	while num > 0:
		num = num // 10
		length = length + 1

	return length


def list_of_multiples(num, length):

	if length == None:
		return []

	else:
		multiples = []

		for i in range(1, length + 1):
			multiple = num * i
			multiples.append(multiple)

		return multiples


def normalize(input_str):
	
	if input_str.isupper():

		input_str = input_str.capitalize()
		input_str = input_str + '!'

	return input_str
		

def cat_dog(num):

	if num % 3 == 0 and num % 5 == 0:
		return 'CatDog'

	elif num % 3 == 0:
		return 'Cat'

	elif num % 5 == 0:
		return 'Dog'

	else:
		return str(num)

