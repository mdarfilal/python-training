import sys
import os

print("bubblesort starting")

#Name of script without path
scriptName = os.path.basename(sys.argv[0]);

usage = "Usage : " + scriptName + "Order tabToSort \n" \
    "Usage : with Order egal asc OR desc \n" \
    "Usage : with tabToSort like : 1,8,74,23"


#Parse values to sort
tab2=list(map(int, sys.argv[2].split(",")))

#Check number of parameters
if(len(sys.argv) < 3):
	print(usage)
	#sys.exit()
	quit()

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
	print ("No function found")
	print(usage)
	quit()

print ("finish")
