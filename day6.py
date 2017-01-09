def get_char():

	t = int(raw_input())

	for i in range(0, t):
	    word = raw_input()
	    first = ""
	    second = ""

	    for i in range(len(word)):
	        if i % 2:
	            second += word[i]

	        else:
	            first += word[i]

	    print "{} {}".format(first, second)

get_char()