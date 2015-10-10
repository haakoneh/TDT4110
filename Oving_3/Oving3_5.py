def solver(a, b, c):
	d = b**2 - 4*a*c
	if(d > 0):
		print('Ligningen {0}x^2 + {1}x + {2} = 0  har to reelle losninger'.format(a, b, c))
	elif(d < 0):
		print('Ligningen {0}x^2 + {1}x + {2} = 0  har to imaginaere losninger'.format(a, b, c))
	else:
		print('Ligningen {0}x^2 + {1}x + {2} = 0  har en reell losning'.format(a, b, c))
	
def main():
	print('Skriv inn en andregradsligning')
	a = float(input())
	b = float(input())
	c = float(input())
	solver(a, b, c)

main()