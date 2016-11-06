import random
"""Draw 6 different values. Loto game"""
loto = []

#Put only 6 values
while (len(loto) != 6):
	#get random value
	x = random.randint(1,46)
	#check if value is not drawn
	if x not in loto:
		loto.append(x)

#print result
print(loto)