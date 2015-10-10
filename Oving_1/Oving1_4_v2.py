msg = 1

def logg(tid, navn, melding):
	print('Msg', msg,',', 'Klokken', tid, 'sendte', navn, 'foelgende melding:', melding)
	global msg
	msg += 1
	
def main():
	# tid = input('Velg tidspunkt:' )
	# navn = input('Velg sender:' )
	# melding = input('Skriv melding:' )
	
	list_tid = ['23:59', '0:00', '0:03', '0:09', '0:09', '0:09']
	list_navn = ['Mr. X', 'Mdm. Evil', 'Dr. Love', 'Mr. X', 'Mr. X', 'Dr. Love']
	list_melding = ['"Har du mottatt pakken?"', '"Ja. Pakken er mottatt."', 
					'"All you need is love!"', '"Dr. Love, love, calling Dr. Love"', 
					'"Dr. Love, Dr. Love wake up now."', '"Up now!"']
	for i in range (0, len(list_tid)):
		logg(list_tid[i], list_navn[i], list_melding[i])
		
if __name__ == '__main__': main()