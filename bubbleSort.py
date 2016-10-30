import sys
import os

print("*******************")
print(" Bubblesort starting")
print("*******************")

#Name of script without path
scriptName = os.path.basename(sys.argv[0])

usage = "Usage : " + scriptName + " Order tabToSort \n" \
	"Usage : with Order egal asc OR desc \n" \
	"Usage : with tabToSort like : 1,8,74,23 \n" \
	"Test usage : " +scriptName+ " test all"

#Variables
nbTestKo=0

ORDER_ASC="asc"
ORDER_DESC="desc"
Test="test"

#Check number of parameters, Three required
if(len(sys.argv) != 3):
	print("Three parameters required")
	print(usage)
	sys.exit()

#Parse values to sort
def parseArgs():
	try:
		tab2=list(map(int, sys.argv[2].split(",")))
	except ValueError:
		print("Can't parse values : ", sys.argv[2])
		print(usage)
		sys.exit()

def sortAscValues():
	parseArgs()
	print("Values to sort asc",tab2)
	tabSortedAsc = sortAsc(tab2)
	print("Values sorted asc",tabSortedAsc)

def sortDescValues():
	parseArgs()
	print("Values to sort desc",tab2)
	tabSortedDesc = sortDesc(tab2)
	print("Values sorted desc",tabSortedDesc)

def sortAsc(array):
	a=0
	while a<len(array)-1:
		i=0
		while i<len(array)-1:
			if (array[i] > array[i+1]):
				array[i], array[i+1] = array[i+1], array[i]
			i+=1
		a+=1
	return array

def sortDesc(array):
	a=0
	while a<len(array)-1:
		i=0
		while i<len(array)-1:
			if (array[i] < array[i+1]):
				array[i], array[i+1] = array[i+1], array[i]
			i+=1
		a+=1
	return array

def compareArray(array, type):
	global nbTestKo
	
	if (type == ORDER_ASC):
		manualSort = sortAsc(array)
		pythonSort = sorted(array)
	else:
		manualSort = sortDesc(array)
		pythonSort = sorted(array, reverse=True)
	
	if (manualSort != pythonSort):
		print("Error in sorting array, expected : ", pythonSort, " but was ",manualSort)
		nbTestKo += 1
		
def allSortTest():
	print("Test all sorts")
	compareArray([1,7,5], ORDER_ASC)
	
	compareArray([1,7,5], ORDER_DESC)
	
	if (nbTestKo==0):
		print("All Tests OK")
	else:
		print(nbTestKo, "tests are KO")

######################################
#				MAIN
######################################

#Check type of sort
if (sys.argv[1]==ORDER_ASC):
	sortAscValues()
elif (sys.argv[1]==ORDER_DESC):
	sortDescValues()
elif (sys.argv[1]==Test and sys.argv[2]=="all"):
	allSortTest()
else:
	print("No function found")
	print(usage)
	sys.exit()
	
print ("Finish")