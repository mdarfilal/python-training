"""Battle dev 8th November 2016, excercise n°1"""

def paire_of_gloves(array):
	#number pair of gloves
	nb_pair = 0
	#delete the first item, which is the number of values
	del array[0]
	#distinct colors
	unique_color_list = list(set(array))
	
	for color in unique_color_list:
		nb_occurence = array.count(color)
		
		if((nb_occurence %2) == 0):
			#if nb_occurence pair, nb_pair equal the half
			nb_pair += nb_occurence/2
		elif(nb_occurence != 1):
			#if nb_occurence not pair, then substract one and nb_pair equal the half
			nb_pair += (nb_occurence-1)/2
	
	#print number of pair existing in the list
	print(nb_pair)

my_array = ["8","rouge", "vert", "bleu", "rouge", "orange", "rouge", "vert", "bleu"]
paire_of_gloves(my_array)