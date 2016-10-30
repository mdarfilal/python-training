import sys
import os

print("*******************")
print(" Bubblesort starting")
print("*******************")

######################################
#				DECLARATIONS
######################################

#Name of script without path
script_name = os.path.basename(sys.argv[0])

usage = "Usage : " + script_name + " Order tab_to_sort \n" \
	"Usage : with Order egal asc OR desc \n" \
	"Usage : with tab_to_sort like : 1,8,74,23 \n" \
	"Test usage : " + script_name + " test all"

#Variables
nb_test_ko=0
tab_to_sort=[]

ORDER_ASC="asc"
ORDER_DESC="desc"
TEST="test"
ALL="all"

#Check number of parameters, Three required
if(len(sys.argv) != 3):
	print("Three parameters required")
	print(usage)
	sys.exit()

######################################
#				FUNCTIONS
######################################

def parse_values_parameter():
	"""Parse values received in the third parameter of script parameters."""
	global tab_to_sort
	try:
		tab_to_sort = list(map(int, sys.argv[2].split(",")))
	except ValueError:
		print("Can't parse values : ", sys.argv[2])
		print(usage)
		sys.exit()

def sort_asc_values():
	"""Print received array in script parameter to sort asc and sort result."""
	parse_values_parameter()
	print("Values to sort asc",tab_to_sort)
	tab_sorted_asc = sort_asc(tab_to_sort)
	print("Values sorted asc",tab_sorted_asc)

def sort_desc_values():
	"""Print received array in script parameter to sort desc and sort result."""
	parse_values_parameter()
	print("Values to sort desc",tab_to_sort)
	tab_sorted_desc = sort_desc(tab_to_sort)
	print("Values sorted desc",tab_sorted_desc)

def sort_asc(array):
	"""Sort asc array given in param.
	@param :  array to sort asc
	@return : array sorted asc
	
	"""
	a = 0
	while a < len(array)-1:
		i = 0
		while i < len(array)-1:
			if(array[i] > array[i+1]):
				array[i], array[i+1] = array[i+1], array[i]
			i += 1
		a += 1
	return array

def sort_desc(array):
	"""Sort desc array given in param.
	@param :  array to sort desc
	@return : array sorted desc
	
	"""
	a = 0
	while a < len(array)-1:
		i = 0
		while i < len(array)-1:
			if(array[i] < array[i+1]):
				array[i], array[i+1] = array[i+1], array[i]
			i += 1
		a += 1
	return array


def compare_array(array, type):
	"""Compare array given in param and the result with python sorted method.
	If the arrays aren't equal, print error and increment test's variable.
	@param :  array to sort
	@param : type of sort (asc or desc)
	
	"""
	global nb_test_ko

	if(type == ORDER_ASC):
		manual_sort = sort_asc(array)
		python_sort = sorted(array)
	else:
		manual_sort = sort_desc(array)
		python_sort = sorted(array, reverse=True)

	if(manual_sort != python_sort):
		print("Error in sorting array, expected : ", python_sort, " but was ",manual_sort)
		nb_test_ko += 1

def all_sorts_test():
	"""Sort Tests method.
	Print if tests are OK or not.
	
	"""
	print("Test all sorts")
	compare_array([1,7,5], ORDER_ASC)
	compare_array([1,7,5], ORDER_DESC)

	if(nb_test_ko == 0):
		print("All Tests OK")
	else:
		print(nb_test_ko, "tests are KO")

######################################
#				MAIN
######################################

#Check type of sort
if(sys.argv[1] == ORDER_ASC):
	sort_asc_values()
elif(sys.argv[1] == ORDER_DESC):
	sort_desc_values()
elif(sys.argv[1] == TEST and sys.argv[2] == ALL):
	all_sorts_test()
else:
	print("No function found")
	print(usage)
	sys.exit()

print("Finish")