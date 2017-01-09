num_entries = input()

entries = {}

for num in range(0, num_entries):
	entry = raw_input()
	entry = entry.split(" ")
	entries[entry[0]] = entry[1]

while True:
	try:
		query = raw_input().strip()
		if query in entries:
			print "{}={}".format(query, entries[query])
		else:
			print "Not found"
	except EOFError:
		break



