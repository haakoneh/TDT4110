def timelonn():
	timelonn = float(input('Skriv inn timelonnen: '))
	timer = float(input('Skriv antall timer: '))
	lonn = timelonn*timer
	print('Lonnen blir: ', lonn)
	
def provisjon():
	grunnlonn = float(input('Skriv inn grunnlonnen: '))
	enhetlonn = float(input('Skriv inn enhetslonnen: '))
	antall = float(input('Skriv antall enheter: '))
	lonn = grunnlonn+(enhetlonn*antall)
	print('Lonnen blir: ', lonn)

def main():
	while True:
		print('Velkommen til ReveNew (tm)')
		check = input('Er den ansatte på [t]imelonn eller [p]rovisjon? ')
		if(check == 't' or check == 'timelonn'):
			timelonn()
			break
		elif(check == 'p' or check == 'provisjon'):
			provisjon()
			break
		else:
			print('Inputmetoden er ugyldig')
			print('Skriv "t" eller "timelonn" for timelonn eller "p" eller "provisjon" for provisjonslonn')
		
main()