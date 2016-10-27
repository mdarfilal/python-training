import sys
import os

print("bubblesort starting")

#Name of script without path
scriptName = os.path.basename(sys.argv[0]);

#Check number of parameters
if(len(sys.argv) < 2):
	print("Usage :" ,scriptName, "tabToSort")
	print("Usage : with tabToSort like : 1,8,74,23")
	#sys.exit()
	quit()
	
#Parse argument
tab2=list(map(int, sys.argv[1].split(",")))

print("Values to sort",tab2)

def sort(array):
	a=0
	while a<len(array)-1:
		i=0
		while i<len(array)-1:
			if (array[i] > array[i+1]):
				array[i], array[i+1] = array[i+1], array[i]
			i+=1
		a+=1
	return array

tabSorted = sort(tab2)
		
print("Values sorted",tabSorted)
print ("finish")