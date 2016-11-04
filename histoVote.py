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
blank_vote = 0

NAME_BLANK_VOTE = "Blank votes"
NAME_FIRST_CANDIDATE = sys.argv[1]
NAME_SECOND_CANDIDATE = sys.argv[2]
NUMBER_OF_CITIZENS = int(sys.argv[3])
CANDIDATES = [NAME_FIRST_CANDIDATE, NAME_SECOND_CANDIDATE]

def vote_of_citizens():
	""" Simulate vote of citizen. """
	global vote_first_candidate
	global vote_second_candidate
	global blank_vote
	
	for i in range(NUMBER_OF_CITIZENS):
		vote = random.randint(1,10)

		if(vote <= 3):
			vote_first_candidate+=1
		elif(vote > 3 and vote <= 6):
			vote_second_candidate+=1
		else:
			blank_vote+=1
	
def show_result_on_stick_graph():
	""" Show the result of vote on a stick graph. """
	print(NAME_FIRST_CANDIDATE, " " ,vote_first_candidate)
	print(NAME_SECOND_CANDIDATE, " " ,vote_second_candidate)

	horizontal_axis = [0,1]	
	width = 1.0
	data = [vote_first_candidate, vote_second_candidate]
	labels = [NAME_FIRST_CANDIDATE, NAME_SECOND_CANDIDATE]

	plt.axis([0,2,0,NUMBER_OF_CITIZENS/2])
	plt.xlabel('Candidates')
	plt.ylabel('Number of votes')
	plt.xticks(horizontal_axis, labels)
	plt.bar(horizontal_axis, data, width, color='g')

	plt.show()

def show_result_on_circular_digram():
	""" Show the result of vote on a circular diagram. """
	print(NAME_FIRST_CANDIDATE, " " ,vote_first_candidate)
	print(NAME_SECOND_CANDIDATE, " " ,vote_second_candidate)

	labels = [NAME_FIRST_CANDIDATE, NAME_SECOND_CANDIDATE, NAME_BLANK_VOTE]
	data = [vote_first_candidate, vote_second_candidate, blank_vote]

	plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True)
	plt.axis('equal')
	plt.show()

print("Who will be the next president")
vote_of_citizens()
#show_result_on_stick_graph()
show_result_on_circular_digram()