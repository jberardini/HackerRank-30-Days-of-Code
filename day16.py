S = raw_input().strip()

try:
	S = int(S)
	print S
	print type(S)

except ValueError:
	print "Bad String"
