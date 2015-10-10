def logg(list_tid, list_navn, list_melding):
	for i in range (0, len(list_tid)):
		print('Msg', i+1,',', 'Klokken', list_tid[i], 'sendte', list_navn[i], 'foelgende melding:', list_melding[i])
	
def main():
	# tid = input('Velg tidspunkt:' )
	# navn = input('Velg sender:' )
	# melding = input('Skriv melding:' )
	
	list_tid = ['23:59', '0:00', '0:03', '0:09', '0:09', '0:09']
	list_navn = ['Mr. X', 'Mdm. Evil', 'Dr. Love', 'Mr. X', 'Mr. X', 'Dr. Love']
	list_melding = ['"Har du mottatt pakken?"', '"Ja. Pakken er mottatt."', 
					'"All you need is love!"', '"Dr. Love, love, calling Dr. Love"', 
					'"Dr. Love, Dr. Love wake up now."', '"Up now!"']
	
	logg(list_tid, list_navn, list_melding)
		
if __name__ == '__main__': main()
