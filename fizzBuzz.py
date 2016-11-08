FIZZ = "Fizz"
BUZZ = "Buzz"

array = list(range(1,101))

for i in range(len(array)):
	"""Print Fizz if number is multiple of three, Buzz if number is multiple of five, FizzBuzz if both of them, else do nothing."""
	mlt_de_3 = (array[i] % 3) == 0
	mlt_de_5 = (array[i] % 5) == 0

	if(mlt_de_3 and mlt_de_5):
		array[i] = FIZZ + BUZZ
	elif(mlt_de_3):
		array[i] = FIZZ
	elif(mlt_de_5):
		array[i] = BUZZ

print(array)