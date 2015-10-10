def gcd(a,b):
	while(b != 0):
		b_old = b
		b = a % b_old
		a = b_old
	return a

def reduce_fraction(a,b, var_gcd):
	a /= var_gcd
	b /= var_gcd
	return a, b
	
def main():
	a = int(input('Skriv inn tall '))
	b = int(input('Skriv inn tall '))
	var_gcd = gcd(a,b)
	print(var_gcd)
	a2, b2 = reduce_fraction(a,b, var_gcd)
	print('For a = {0} og b = {1} skriver programmet ut: {2}/{3}'.format(a, b, a2, b2))
	
main()