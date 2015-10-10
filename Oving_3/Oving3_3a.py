import math

def sirkel(r):
	areal = math.pi*r**2
	omkrets = 2*math.pi*r
	print('Areal: ', "%.2f" % areal)
	print('Omkrets: ', "%.2f" % omkrets) 
	
def main():
	r = float(input('Skriv radius for sirkel: '))
	sirkel(r)

main()