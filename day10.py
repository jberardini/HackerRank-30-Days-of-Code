def convert(n):
	
	binary = ''
	while n > 0:
		digit = str(n % 2)
		binary = digit + binary
		n = n / 2

	return binary

def get_consecutive(binary):
	max_count = 0
	current_count = 0


	for char in binary:
		if char == '1':
			current_count += 1
			max_count = max(current_count, max_count)
		else:
			current_count = 0

	print max_count

binary = convert(5)
print binary
get_consecutive(binary)

binary2 = convert(13)
get_consecutive(binary2)


"""For HackerRank"""
def get_consecutive2(n):
	binary = ''
	while n > 0:
		digit = str(n % 2)
		binary = digit + binary
		n = n / 2

	max_count = 0
	current_count = 0


	for char in binary:
		if char == '1':
			current_count += 1
			max_count = max(current_count, max_count)
		else:
			current_count = 0

	print max_count

get_consecutive2(5)
get_consecutive2(13)