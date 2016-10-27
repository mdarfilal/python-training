import sys
import os

print("*******************")
print("bubblesort starting")
print("*******************")

#Name of script without path
scriptName = os.path.basename(sys.argv[0]);

Usage = """Usage : ,scriptName, Order tabToSort
Usage : with Order egal asc OR desc
Usage : with tabToSort like : 1,8,74,23"""

#Check number of parameters, Three required
if(len(sys.argv) != 3):
	print("Three parameters required")
	print(Usage)
	sys.exit()

#Parse values to sort
try:
	tab2=list(map(int, sys.argv[2].split(",")))
except ValueError:
	print("Can't parse values : ", sys.argv[2])
	print(Usage)
	sys.exit()

def sortAscValues():
	print("Values to sort asc",tab2)
	tabSortedAsc = sortAsc(tab2)
	print("Values sorted asc",tabSortedAsc)

def sortDescValues():
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

######################################
#				MAIN
######################################

#Check type of sort
if (sys.argv[1]=="asc"):
	sortAscValues()
elif (sys.argv[1]=="desc"):
	sortDescValues()
else:
	print("No function found")
	print(Usage)
	sys.exit()
	
print ("finish")