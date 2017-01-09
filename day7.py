def reverse_arr():
	n = int(raw_input().strip())
	arr = map(int,raw_input().strip().split(' '))
	reversed_arr = []
	printed = ''

	for num in arr:
	    reversed_arr.insert(0, num)

	for num in reversed_arr:
	    str_num = str(num)
	    printed += str_num + " "

	print printed

reverse_arr()