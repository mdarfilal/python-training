import sys
import os

#Name of script without path
script_name = os.path.basename(sys.argv[0])

SIMPLE_USAGE = "Simple usage : " +script_name
PERSONNAL_USAGE = "Peronnal usage : " +script_name+ "Number_min Number_max"
USAGE = SIMPLE_USAGE+"\n"+PERSONNAL_USAGE

FIZZ = "Fizz"
BUZZ = "Buzz"

if(len(sys.argv) != 3 and len(sys.argv) != 1):
	print(USAGE)
elif(len(sys.argv) == 3):
	nb_min = int(sys.argv[1])
	nb_max = int(sys.argv[2]) +1
	array = list(range(nb_min, nb_max))
else:
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