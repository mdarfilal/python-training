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

WHITE_VOTE = "White votes"
NAME_FIRST_CANDIDATE = sys.argv[1]
NAME_SECOND_CANDIDATE = sys.argv[2]
NUMBER_OF_CITIZENS = int(sys.argv[3])
CANDIDATES = [NAME_FIRST_CANDIDATE, NAME_SECOND_CANDIDATE]

def vote_of_citizens():
	""" Simulate vote of citizen. """
	global vote_first_candidate
	global vote_second_candidate

	for i in range(NUMBER_OF_CITIZENS):
		vote = random.randint(1,10)
		random.shuffle(CANDIDATES)
		if(CANDIDATES[0] == NAME_FIRST_CANDIDATE and vote == 1):
			vote_first_candidate+=1
		elif(CANDIDATES[0] == NAME_SECOND_CANDIDATE and vote == 2):
			vote_second_candidate+=1

def calculate_white_vote():
	""" Calculate number of white votes. """
	global white_vote
	white_vote = NUMBER_OF_CITIZENS - vote_first_candidate - vote_second_candidate
	
def show_result_on_stick_graph():
	""" Show the result of vote on a stick graph. """
	print(vote_first_candidate)
	print(vote_second_candidate)

	horizontal_axis = [0,1]	
	width = 1.0
	data = [vote_first_candidate, vote_second_candidate]
	labels = [NAME_FIRST_CANDIDATE, NAME_SECOND_CANDIDATE]

	plt.axis([0,2,0,NUMBER_OF_CITIZENS/4])
	plt.xlabel('Candidates')
	plt.ylabel('Number of votes')
	plt.xticks(horizontal_axis, labels)
	plt.bar(horizontal_axis, data, width, color='g')

	plt.show()

def show_result_on_circular_digram():
	""" Show the result of vote on a circular diagram. """
	print(vote_first_candidate)
	print(vote_second_candidate)

	labels = [NAME_FIRST_CANDIDATE, NAME_SECOND_CANDIDATE, WHITE_VOTE]
	data = [vote_first_candidate, vote_second_candidate, white_vote]

	plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True)
	plt.axis('equal')
	plt.show()

print("Who will be the next president")
vote_of_citizens()
calculate_white_vote()
#show_result_on_stick_graph()
show_result_on_circular_digram()