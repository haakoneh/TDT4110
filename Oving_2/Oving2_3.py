def convert(fahrenheit):
	celsius = (fahrenheit-32)/(9/5)
	print ('Temperaturen i celsius: ', celsius)

def main():
	fahrenheit = float(input('Skriv inn temperaturen i fahrenheit: ' ))
	convert(fahrenheit)
	
main()