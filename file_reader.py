




def get_train_parameters(filename, line_number=1):
	file = open(filename,'r')
	i=0
	X = []
	y = []

	for line in file:
		if (i == 0):
			pass
		else:	
			vec = line.split('\n')
			vec.remove("")
			tempX = []
			
			for string in vec:
				vec = string.split(',')
			for index in range(len(vec)):
				if(index==5):
					tempY = vec[index]
				else:
					tempX.append(vec[index])
			
			X.append(tempX)
			y.append(tempY)

		i+=1
		if(i >line_number):
			break

	return X,y



# def get_train_parameters(filename, line_number=1):
	file = open(filename,'r')
	i=0
	X = []
	y = []

	for line in file:
		if (i == 0):
			pass
		else:	
			vec = line.split('\n')
			vec.remove("")
			tempX = []
			
			for string in vec:
				vec = string.split(',')
			for index in range(len(vec)):
				if(index==3):
					tempY = vec[index]
				else:
					tempX.append(vec[index])
			
			X.append(tempX)
			y.append(tempY)

		i+=1
		if(i >line_number):
			break

	return X,y

# def get_test_parameters(filename, line_number=1):
	file = open(filename,'r')
	i=0
	X = []
	y = []

	for line in file:
		if (i == 0):
			pass
		else:	
			vec = line.split('\n')
			vec.remove("")
			tempX = []	
			for string in vec:
				vec = string.split(',')
			for index in range(len(vec)):
				tempX.append(vec[index])
			
			X.append(tempX)		
		i+=1
		# if(i >line_number):
		# 	break

	return X

def get_test_parameters(filename, line_number=1):
	file = open(filename,'r')
	i=0
	X = []
	y = []

	for line in file:
		if (i == 0):
			pass
		else:	
			vec = line.split('\n')
			vec.remove("")
			tempX = []	
			for string in vec:
				vec = string.split(',')
			for index in range(len(vec)):
				tempX.append(vec[index])
			
			X.append(tempX)		
		i+=1
		if(i >line_number):
			break

	return X


def print_file(filename, line_number=1):
	file = open(filename,'r')
	print(filename+"\n")
	i = 0
	vec = []
	for line in file:
		i+=1
		print (line+'\n')
		# if(i >= line_number):
		# 	break


