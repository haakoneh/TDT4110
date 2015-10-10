def billettPris(alder):
	if(alder < 5 or alder > 60):
		print('Du reiser gratis!')
	elif(alder >= 5 and alder <= 15):
		print('Prisen for deg er 15 kr')
	elif(alder > 15 and alder <= 20):
		print('Prisen for deg er 20 kr')
	elif(alder > 20 and alder <= 25):
		print('Prisen for deg er 30 kr')
	elif(alder > 25 and alder <= 60):
		print('Prisen for deg er 40 kr')		

def main():
	while True:
		alder = int(input('Skriv inn alder for bilettpris: '))
		billettPris(alder)

main()