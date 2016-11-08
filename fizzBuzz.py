MULT_DE_3 = "Fizz"
MULT_DE_5 = "Buzz"

array = list(range(1,101))

def multiple_de_cinq(number):
	"""Return True if parameter is multiple of five, else return False."""
	unite = number%10
	if(unite == 5 or unite == 0):
		return True
	
	return False
	
def multiple_de_trois(number):
	"""Return True if parameter is multiple of three, else return False."""
	# variable = number
	# somme = 0
	# while (variable != 0):
		# print("s1 " ,somme)
		# print("v1 " ,variable)
		# somme += variable%10
		# print("s2 " ,somme)
		# print("v2 " ,variable)
		# variable = int(variable / 10)
		# print("v3 " ,variable)
	result = 0
	x = number / 3
	
	if(int(x) != 0):
		result = number / int(x)
	
	if(result == 3):
		return True
			
	return False

for i in range(len(array)):
	"""Print Fizz if number is multiple of three, Buzz if number is multiple of five, FizzBuzz if both of them, else do nothing."""
	mlt_de_3 = multiple_de_trois(array[i])
	mlt_de_5 = multiple_de_cinq(array[i])

	if(mlt_de_3 and mlt_de_5):
		array[i] = MULT_DE_3 + MULT_DE_5
	elif(mlt_de_3):
		array[i] = MULT_DE_3
	elif(mlt_de_5):
		array[i] = MULT_DE_5

print(array)