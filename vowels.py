import argparse
def ArgParser(): 
	# Argument Passing Process 
	parser = argparse.ArgumentParser(description = 'Vowels Operation')
	parser.add_argument('path', help = 'Name or Path of file')
	args = parser.parse_args()
	return args

def main():
	#Vowels Program in Python
	Args = ArgParser()
	fileName = Args.path
	FileName =open(fileName,"r")
	File = list(FileName)
	# Initial Values of Count
	count_a_or_A=0 
	count_e_or_E=0 
	count_i_or_I=0 
	count_o_or_O=0 
	count_u_or_U=0

	# for Checking Process of VOWELS
	for i in range (0,len(File)):	
		for j in range(0,len(File[i])):	
			if(('A'== File[i][j]) or ('a'==File[i][j])):
				count_a_or_A +=1
			elif(('E' == File[i][j]) or ('e' == File[i][j])):
				count_e_or_E+=1
			elif(('I'== File[i][j]) or ('i' == File[i][j])):
				count_i_or_I+=1
			elif(('O'== File[i][j]) or ('o' == File[i][j])):
				count_o_or_O+=1
			elif(('U'== File[i][j]) or ('u' == File[i][j])):
				count_u_or_U+=1
	#else:
	#	print "There is no Vowels"
	print "A or a Count is:",count_a_or_A
	print "E or e Count is:",count_e_or_E
	print "I or i Count is:",count_i_or_I
	print "O or o Count is:",count_o_or_O
	print "U or u Count is:",count_u_or_U

	

if __name__ == '__main__':
	main()