def add_numb(n):
	i, j, k = 0, 0, 0
	while True:
		i += 1
		k += i ** 2
		if(k > n):
			return i-1, j
		j = k
		
def main():
	n = int(input('Skriv inn tall '))
	i, j = add_numb(n)
	print('Antall elementer ' + str(i) + ', stoerste tall blir ' + str(j))

main()