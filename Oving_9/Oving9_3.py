def add_birthday_to_date (birthdays, date, name): #Legger til navn ved gitt dato
	try: #Skjekker om dato, og liste eksisterer
		birthdays[date].append(name)
	except AttributeError: #Dersom liste ikke eksisterer 
		birthdays[date] = [birthdays[date], name]
	except KeyError: #Dersom nokkel ikke eksisterer 
		birthdays[date] = name
	# print(birthdays) #Printer dicitonary 
	
def main():
	birthdays = {
		'22 nov': ['Lars', 'Mathias'],
		'10 des': ['Elle'],
		'30 okt': ['Veronica', 'Rune'],
		'12 jan': 'Silje',
		'31 okt': ['Willy'],
		'8 jul': ['Brage', 'Oystein'],
		'1 mar': 'Nina'}
	add_birthday_to_date(birthdays, '12 jan', 'Sindre')
	add_birthday_to_date(birthdays, '9 feb', 'Lillian')
	print(birthdays) #Printer dicitonary 
	
main()