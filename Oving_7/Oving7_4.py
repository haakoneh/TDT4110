def string_check(string1, string2):
	tmp1 = string1.split()
	tmp2 = string2.split()
	if(len(tmp1) != len(tmp2)): 
		return False
	else:
		for i in range(0, len(tmp1)):
			if(tmp1[i] != tmp2[i]):
				return False
	return True

def palindrome(string):
	if len(string) < 1:
		return True
	else:
		if string[0] == string[-1]:
			return palindrome(string[1:-1])
		else:
			return False

def in_string(string1, string2):
	if string1 in string2:
		return True
	return False

def main():
	string1 = ('Hallo alle sammen!')
	string2 = ('Hallo alle samen!')
	string3 = ('Hallo alle!')
	
	print(string_check(string1, string1)) 
	print(string_check(string1, string2)) 
	print(string_check(string1, string3)) 
	
	print(palindrome(''))
	print(palindrome('abab'))
	print(palindrome('abba'))
	
	print(in_string('Hallo', string1))
	print(in_string('hallo', string1))
	
main()