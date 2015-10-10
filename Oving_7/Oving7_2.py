def numb_lines(fname):
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
	return i + 1
	
def numb_listmake(fname):
	numb_list = []
	with open(fname) as f:
		for i, l in enumerate(f):
			temp = l.split()
			for j in range(0, len(temp)):
				if(temp[j] in numb_list):
					pass
				else: numb_list.append(temp[j])
	return numb_list
	
def string_listmake(fname):
	numb_list = []
	with open(fname) as f:
		for i, l in enumerate(f):
			temp = l.split()
			for j in range(0, len(temp)):
				numb_list.append(temp[j])
	return numb_list

def numb_occurrence(list1, list2):
	for i in range(0, len(list1)):
		x = list2.count(list1[i])
		print(list1[i], ': ', x)

def main():
	fname = 'exercise2.txt'
	print(numb_lines(fname))
	numb_list = numb_listmake(fname)
	string = string_listmake(fname)
	numb_occurrence(numb_list, string)
	
main()
