def print_coins(coin_list):
	print('Antall 20 mynter ', coin_list[0])
	print('Antall 10 mynter ', coin_list[1])
	print('Antall 5 mynter ', coin_list[2])
	print('Antall 1 mynter ', coin_list[3])
	print('Antall 0.5 mynter ', coin_list[4])
	print('-------------------------')

def find_coins(tooth):
	coin_list = [0, 0, 0, 0, 0]
	while(tooth >= 40): #20 mynt
		coin_list[0] += 1
		tooth -= 40
	while(tooth >= 20): #10 mynt
		coin_list[1] += 1
		tooth -= 20
	while(tooth >= 10): #5 mynt
		coin_list[2] += 1
		tooth -= 10
	while(tooth >= 2): #1 mynt
		coin_list[3] += 1
		tooth -= 2
	while(tooth >= 1): #.5 mynt
		coin_list[4] += 1
		tooth -= 1
	print_coins(coin_list)
	
	
def main():
	teeth = [95 , 103 , 71 , 99 , 114 , 64 , 95 , 53 , 97 , 114 ,
			109 , 11 , 2, 21 , 45 , 2, 26 , 81 , 54 , 14 ,
			118 , 108 , 117 , 27 , 115 , 43 , 70 , 58 , 107]
	for i in range (0, len(teeth)):
		find_coins(teeth[i])
	# find_coins(teeth[0])

main()
