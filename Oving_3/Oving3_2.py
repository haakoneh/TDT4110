debug = False 

def add(a, b):
	#global debug
	if((a == 4 and b == 7) or (a == 4 and b == 7)):
		debug = True
	#else:
	#	debug = False
	if debug:
		print('Tallene som summmeres er ', a, ' og ', b)
	print(a+b)		

def main():
	a = int(input())
	b = int(input())
	add(a,b)
	
main()
