import sys
import os
import matplotlib.pyplot as plt
import random

#Name of script without path
script_name = os.path.basename(sys.argv[0])

usage = "Usage : " + script_name + " name_first_candidate name_second_candidate  number_of_citizens"

#Check number of parameters, Three required
if(len(sys.argv) != 4):
	print("Four parameters required")
	print(usage)
	sys.exit()

vote_first_candidate = 0
vote_second_candidate = 0

name_first_candidate = sys.argv[1]
name_second_candidate = sys.argv[2]
number_of_citizen = int(sys.argv[3])
candidates = [name_first_candidate, name_second_candidate]

def vote_of_citizens():
	""" Simulate vote of citizen. """
	global vote_first_candidate
	global vote_second_candidate
	
	for i in range(number_of_citizen):
		vote = random.randint(1,10)
		random.shuffle(candidates)
		if(candidates[0] == name_first_candidate and vote == 1):
			vote_first_candidate+=1
		elif(candidates[0] == name_second_candidate and vote == 2):
			vote_second_candidate+=1

def show_result_of_vote():
	""" Show the result of vote on a stick graph. """
	x = [0,1]
	
	print(vote_first_candidate)
	print(vote_second_candidate)
	height = [vote_first_candidate, vote_second_candidate]
	width = 1.0
	labels = [name_first_candidate, name_second_candidate]
	
	plt.axis([0,2,0,number_of_citizen/4])
	plt.xlabel('Candidates')
	plt.ylabel('Number of votes')
	plt.xticks(x, labels)
	plt.bar(x, height, width, color='g')
	plt.show()

vote_of_citizens()
show_result_of_vote()