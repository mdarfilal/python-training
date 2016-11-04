import sys
import os
from datetime import datetime

DATE_FORMAT = "date format : DD/MM/YYYY"
SIZE_FORMAT = "size format in cm: 50,00"
WEIGHT_FORMAT = "weight format in Kg: 3,000"
EXIT_USAGE = "Exit usage : only write exit"
USAGE = "Usage : date size weight \n" +DATE_FORMAT+"\n"+SIZE_FORMAT+"\n"+WEIGHT_FORMAT+"\n"+EXIT_USAGE

EXIT = "exit"

date = None
size = None
weight = None

def exit_program():
	""" Exit program. """
	sys.exit()

def check_values(str_datas):
	""" Verify number of parameters and coherence. """
	datas = list(map(str, str_datas.split(" ")))

	if(len(datas) == 1 and datas[0] == EXIT):
		exit_program()
	elif(len(datas) != 3):
		print(USAGE)
		return None
	else:
		return datas

def parse_values(datas):
	""" Convert all values in good format, date in date, size in float, weight in float. """
	global date
	global size
	global weight
	
	date = datas[0]
	size = datas[1]
	weight = datas[2]
	
	try:
		datetime.strptime(date, '%d/%m/%Y')
	except ValueError:
		print("Can't parse date : ", date)
		print(DATE_FORMAT)
	
while(True):
	str_datas = input('Input date size weight (or "exit" to quit): ')
	datas = check_values(str_datas)
	if(datas is not None):
		parse_values(datas)
		print("Vous avez saisi : ",datas)