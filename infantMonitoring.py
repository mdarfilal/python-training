import sys
import os
from datetime import datetime
import csv
from matplotlib import pyplot as plt

DATE_FORMAT = "date format : DD/MM/YYYY"
SIZE_FORMAT = "size format in cm: 50.00"
WEIGHT_FORMAT = "weight format in Kg: 3.000"
EXIT_USAGE = "Exit usage : only write exit"
USAGE = "Usage : date size weight \n" +DATE_FORMAT+"\n"+SIZE_FORMAT+"\n"+WEIGHT_FORMAT+"\n"+EXIT_USAGE

DATE_FORMATTER = '%d/%m/%Y'
EXIT = "exit"

date = None
size = None
weight = None

date_list = []
size_list = []
weight_list = []
	
file_name = "infant_monotoring.csv"

def exit_program():
	""" Exit program."""
	sys.exit()

def check_values(str_datas):
	""" Verify number of parameters and coherence."""
	datas = list(map(str, str_datas.split(" ")))

	if(len(datas) == 1 and datas[0] == EXIT):
		exit_program()
	elif(len(datas) != 3):
		print(USAGE)
		return None
	else:
		return datas

def parse_values(datas):
	""" Convert all values in good format, date in date, size in float, weight in float."""
	global date
	global size
	global weight

	try:
		datetime.strptime(datas[0], DATE_FORMATTER)
		date = datas[0]
	except ValueError:
		print("Can't parse date : ", datas[0])
		print(DATE_FORMAT)
		return False

	try:
		size = float(datas[1])
	except ValueError:
		print("Can't convert : ", datas[1])
		print(SIZE_FORMAT)
		return False

	try:
		weight = float(datas[2])
	except ValueError:
		print("Can't convert : ", datas[2])
		print(WEIGHT_FORMAT)
		return False

	return True

def create_file():
	"""Create csv file if not exist."""
	print("Create file")
	#open file
	file = open(file_name, "w", newline ='')

	try:
		#create writer
		writer = csv.writer(file, delimiter=';')

		#write
		writer.writerow(("Date", "Size", "Weight"))

	finally:
		#close file
		file.close()

def write_file():
	"""Write values entered with keyboard into csv file."""
	print("Write into file")
	
	#open file and write a new line whitout white line
	file = open(file_name, "a", newline ='')

	try:
		#create writer
		writer = csv.writer(file, delimiter=';')
		
		writer.writerow((date, size, weight))
	finally:
		#close file
		file.close()

def read_file():
	"""Read csv file."""
	print("Read file")

	global date_list
	global size_list
	global weight_list
	
	with open(file_name, 'r') as file:
		reader = csv.reader(file, delimiter=';')
		#skip the header
		next(reader, None)
		for row in reader:
			print(row)
			date_list.append(datetime.strptime(row[0], DATE_FORMATTER))
			size_list.append(float(row[1]))
			weight_list.append(float(row[2]))

def create_graph():
	"""Create graph thanks to csv values."""
	plt.title('Infant Monitoring Graph')
	plt.subplot(211)
	plt.plot(date_list,weight_list,'g')
	plt.xlabel('date')
	plt.ylabel('weight (Kg)')
	
	plt.subplot(212)
	plt.plot(date_list,size_list,'r')	
	plt.xlabel('date')
	plt.ylabel('size (cm)')
	
	plt.show()

while(True):
	str_datas = input('Input date size weight (or "exit" to quit): ')
	datas = check_values(str_datas)
	if(datas is not None):
		parsed = parse_values(datas)
		if(parsed is True):
			if not(os.path.isfile(file_name)):
				create_file()
			write_file()