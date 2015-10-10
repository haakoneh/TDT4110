def printValues(dict, key):
	print(dict[key])

def string_check(string1, string2): #Skjekker om to strenger er like
	tmp1 = string1.split() #Setter tegnene i en string i en liste
	tmp2 = string2.split() #Setter tegnene i en string i en liste
	for i in range(len(tmp1)): #Traverserer gjennom liste
		if(tmp1[i] != tmp2[i]): #Skjekker om tegnene er like
			return False #Returnerer FALSE hvis ikke
	return True #Returnerer TRUE hvis de er like
	
def findInfected(dict, list): #Finner infisert ost
	infected = [] #Ny tom liste
	for key, value in dict.iteritems(): #Traverserer gjennom verdiene i dictionary
		for i in list: #Traverserer gjennom liste
			for j in value: #Traverserer gjennom tuppel
				if string_check(i, j): #Skjekker om stringene er like
					infected.append(key) #Legger til i liste, hvis ja
					break #Avslutter, for aa unngaa flere av samme ost
	return infected #Returnerer ny liste

def findUninfected(dict, list): #Finner uinfisert ost
	uninfected = [] #Ny tom liste
	for key in dict: #Traverserer gjennom dictionary
		for i in list: #Traverserer gjennom liste
			if string_check(key, i): #Skjekker noklene mot de infiserte ostene
				uninfected.append(key) #Legger til i liste, hvis uinfisert
				break #Avslutter, for aa unngaa flere av samme ost
	return uninfected #Returnerer ny liste
	
def main():
	cheeses = {
		'cheddar':
			('A235 -4', 'A236 -1', 'A236 -2', 'A236 -3', 'A236 -5', 'C31 -1', 'C31 -2'	),
		'mozarella':
			('Q456 -9', 'Q456 -8', 'A234 -5', 'Q457 -1', 'Q457 -2'),
		'gombost':
			('ZLAFS55 -4', 'ZLAFS55 -9', 'GOMBOS -7', 'A236 -4'),
		'geitost':
			('SPAZ -1', 'SPAZ -3', 'EMACS45 -0'),
		'port salut':
			('B15 -1', 'B15 -2', 'B15 -3', 'B15 -4', 'B16 -1', 'B16 -2', 'B16 -4'),
		'camembert':
			('A243 -1', 'A234 -2', 'A234 -3', 'A234 -4', 'A235 -1', 'A235 -2', 'A235 -3'),
		'ridder':
			('GOMBOS -4', 'B16 -3')}
	printValues(cheeses, 'port salut') #Skriver ut hyller for 'port salut'
	infected_list = ['A234', 'A235', 'B13', 'B14', 'B15', 'C31'] #Liste over infiserte hyller
	infected_cheeses = findInfected(cheeses, infected_list)
	print(infected_cheeses)
	print(findUninfected(cheeses, infected_cheeses))
	
main()