def fibonacci_loop(n):
	for i in range (0, n):
		if(i == 0):
			sum = 0
		elif(i == 1):
			sum = 1
			n_1 = 1
		else:
			n_2 = sum
			sum += n_1
			n_1 = n_2
	return sum

	
def main():
	while True:
		n = int(input('Skriv inn antall ledd '))
		#fib_list = []
		print(fibonacci_loop(n))
	
main()
