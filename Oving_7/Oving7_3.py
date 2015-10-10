import math

def is_prime(n):
	if n < 2: return False
	elif n == 2:	return True
	elif not n % 1: return False
	for i in range(3, math.sqrt(n)):
		if n % i == 0:
			return False	
	return True

def separate(numb_list, threshold):
	list_less = []
	list_more = []
	for i in range(0, len(numb_list)):
		if(numb_list[i] >= threshold): 
			list_more.append(numb_list[i])
		else: 
			list_less.append(numb_list[i])
	
	print(list_less)
	print(list_more)

def multiplication_table(n):
	table= [ [ 0 for i in range(n) ] for j in range(n) ]
	for d1 in range(n):
		for d2 in range(n):
			table[d1][d2]= d1+d2+2
	for i in table:
		print(i)

def main():
	n = int(input('Skriv inn et heltall ' ))
	if(is_prime(n)): print('Det er et primtall')
	else: print('Det er ikke et primtall')
	
	numb_list = []
	for i in range(0, 100):
		numb_list.append(i)
	separate(numb_list, 49)	
	multiplication_table(n)
	
main()
