ant_kvinner, ant_menn = 0, 0
ant_sosmedier, ant_facebook = 0, 0 
tid_sosmedier = 0

def main():
	while True:
		global ant_kvinner 
		global ant_menn 
		global ant_sosmedier
		global ant_facebook  
		global tid_sosmedier 
				
		kjonn = input('Skriv inn "k" for kvinne, "m" for mann ')
		if(kjonn == 'k'):
			ant_kvinner += 1
		elif(kjonn == 'm'):
			ant_menn += 1
		elif(kjonn == 'hade'):
			break
		else:
			continue
		
		alder = input('Skriv inn alder ')
		if(alder == 'hade'): break
		alder = int(alder)
		if(alder < 16 or alder > 25):
			print('Du er utenfor aldersgruppen')
			continue
		sos_svar = input('Bruker du et, eller flere sosiale medier, "ja" eller "nei" ')
		
		if(sos_svar == 'ja'):
			ant_sosmedier += 1
			if(kjonn == 'k'):
				medlem_facebook = input('Mellom 55-60% av Facebook sine brukere er kvinner. Er du en av disse? ')			
			else:
				medlem_facebook = input('Mellom 40-45% av Facebook sine brukere er menn. Er du en av disse? ')
			if(medlem_facebook == 'hade'):
				break
			elif(medlem_facebook == 'ja'):
				ant_facebook += 1	
			timer_sosmedier = int(input('Hvor mange timer bruker du paa sosiale timer? '))
			tid_sosmedier += timer_sosmedier
		elif(sos_svar == 'hade'):
			break
		
	print('Antall kvinner ', ant_kvinner)
	print('Antall menn ',ant_menn)
	print('Antall sosiale medier ', ant_sosmedier) 
	print('Antall facebook ', ant_facebook)
	print('Tid sosiale medier ', tid_sosmedier)

main()
