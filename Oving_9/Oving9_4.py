def findAlle(fname): #Finner studier med grense med 'Alle'
	i = 0 #Setter teller
	f = open(fname, "r") #Apner fil
	lines = f.readlines() #Plasserer alle linjer i filen i en liste
	for s in lines: #Traverser liste
		studie = s.split(',') #Splitter linjen
		if studie[1] == '"Alle"\n': #Skjekker om poengrensen er "Alle"
			i += 1 #Oker teller med 1
	f.close()
	return i #Returner ant poengrenser med "Alle"

def averageScore(fname):
	i, j = 0, 0 #Setter tellere
	f = open(fname, "r") #Aepner fil
	lines = f.readlines()#Plasserer alle linjer i filen i en liste
	for s in lines: #Traverser liste
		studie = s.split(',') #Splitter linjen
		if studie[1] != '"Alle"\n': #Skjekker om poengrensen er "Alle"
			i += float(studie[1]) #Summere poengrensene 
			j += 1 #Oker teller med 1
	f.close()
	return i/j #Returnerer gjennomsnitt

def findMaxMin(fname):
	max, min = 0, 0 #Setter tellere
	f = open(fname, "r") #Setter teller
	# lines = f.readlines()#Plasserer alle linjer i filen i en liste
	for s in f: #Traverser liste
		studie = s.split(',') #Splitter linjen
		if studie[1] != '"Alle"\n': #Skjekker om poengrensen er "Alle"
			poeng = float(studie[1]) #Transformerer til float
			if max == 0 and min == 0: #Skjekker om max og min har verdier
				max = poeng #Setter variabel
				min = poeng #Setter variabel
			elif poeng > max: #Skjekker ny max
				max = poeng #Setter variabel
			elif poeng < min: #Skjekker ny min
				min = poeng #Setter variabel
	f.close()
	return (max, min) #Returner max og min
	
def main():
	fname = 'poenggrenser_2011.csv'
	print('Antall studier med grense "Alle": ' + str(findAlle(fname)))
	print('Gjennomsnitt for poenggrense: ' + str("%.2f" % averageScore(fname)))
	print('Max- og minverdi for poenggrenser: ' + str(findMaxMin(fname)))
	
main()