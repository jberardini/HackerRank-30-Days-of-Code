def print_cond(n):
	if n % 2:
		print 'Weird'
	elif n >=2 and n <= 5:
		print 'Not Weird'
	elif n >= 6 and n <= 20:
		print 'Weird'
	elif n > 20:
		print 'Not Weird'

print_cond(24)
print_cond(3)