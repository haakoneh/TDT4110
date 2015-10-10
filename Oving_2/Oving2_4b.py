def intCheck(check):
	if(check > 0):
		print('Tallet er positivt')
	elif(check < 0):
		print('Tallet er negativt')
	else:
		print('Tallet er 0')

def main():
	check = float(input('Skriv inn et tall: '))
	intCheck(check)
	
main()