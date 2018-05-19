
def factorial(num): 
	if num >= 0:
		if num == 0:
			return 1
		return num * factorial(num -1)
	else:
		return -1