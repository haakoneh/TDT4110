def main():
	li = [1, 2, 3, 4, 5, 6]
	for i in range (0, 6):
		if i % 2 == 0:
			li[i] *= -1
	# li.sort()
	for i in range (0, 6):
		print(str(li[i]))
	li.reverse()
	for i in range (0, 6):
		print(str(li[i]))

main()