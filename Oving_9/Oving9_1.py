def shortform(list, long, short):
	short_list = [] #Ny tom liste
	for i in list: #Traverserer gjennom liste
		short_list.append(i.replace(long,short)) #Erstatter gitt string, og plasserer i ny liste
	return short_list #Returnerer ny liste

def main():
	videoer = ['http://www.youtube.com/watch?v=oKI-tD0L18A',
		'http://www.youtube.com/watch?v=oHg5SJYRHA0',
		'http://www.youtube.com/watch?v=82LCKBdjywQ',
		'http://www.youtube.com/watch?v=GpNSip5gyKo',
		'http://www.youtube.com/watch?v=rHG-JO8gIGk',
		'http://www.youtube.com/watch?v=OZBWfyYtYQY']
	
	long = 'http://www.youtube.com/watch?v=' #Det som skal byttes ut
	short = 'youtu.be/' #Det som skal settes inn
	print(shortform(videoer, long, short)) #Sender inn liste, hva som skal byttes ut, og hva som skal settes inn

main()