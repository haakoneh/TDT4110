import math

def vector_list(a, b, c):
	l = [a, b, c]
	return l
	
def vector_print(vec):
	print('Vakker vektor: (' + str(vec[0]) + ', ' + str(vec[1]) + ', ' + str(vec[2]) + ')')

def scalar_multi(vec1, scal):
	scal_sum = []
	for i in range (0,3):
		sum = vec1[i]*scal
		scal_sum.append(sum)
	return scal_sum
	
def dot_product(vec1, vec2):
	dot = 0
	for i in range (0,3):
		dot += vec1[i]*vec2[i]
	return dot

def vector_lenght(vec):
	lenght = 0
	for i in range (0,3):
		lenght += vec[i]**2
	return math.sqrt(lenght)
	
def scal_compare(scal1, scal2):
	i = scal1/scal2 
	print('Forholdet blir ' "%.2f" % i)
	
def vector_reg():
	a = int(input('Skriv inn a for vektoren '))
	b = int(input('Skriv inn b for vektoren '))
	c = int(input('Skriv inn c for vektoren '))
	return vector_list(a, b, c)
	
def main():
	vec1 = vector_reg()
	
	print(vector_lenght(vec1))
	
	print(vector_print(vec1))
	
	sca1 = int(input('Skalar 1 '))
	scal1 = scalar_multi(vec1, sca1)
	print(scal1)
	
	l1 = vector_lenght(vec1)
	l2 = vector_lenght(scal1)
	print(l1)
	print(l2)
	scal_compare(l1, l2)
	
	vec2 = vector_reg()
	
	dot = dot_product(vec1, vec2)
	print(dot)
main()